#!/usr/bin/env python3
"""
Standalone Qwen 14B inference script
Reads hard examples CSV, runs inference, saves results
"""

import os
import sys
import pandas as pd
import numpy as np
import torch
import vllm
from vllm.lora.request import LoRARequest
from logits_processor_zoo.vllm import MultipleChoiceLogitsProcessor
from scipy.special import softmax

def main():
    MODEL_NAME = "/kaggle/input/qwen2.5/transformers/14b-instruct-gptq-int4/1"
    LORA_PATH = "/kaggle/input/lora_14b_gptq_1epoch_r32/keras/default/1"

    print("=" * 80)
    print("Starting Qwen 14B Inference")
    print("=" * 80)

    print("\n[1/5] Loading hard examples...")
    df_hard = pd.read_csv('hard_examples.csv')
    print(f"Loaded {len(df_hard)} hard examples")
    print(f"Columns: {df_hard.columns.tolist()}")

    print("\n[2/5] Initializing Qwen 14B model...")
    llm = vllm.LLM(
        MODEL_NAME,
        quantization='gptq',
        tensor_parallel_size=torch.cuda.device_count(),
        gpu_memory_utilization=0.98,
        trust_remote_code=True,
        dtype="half",
        enforce_eager=True,
        max_model_len=4096,
        disable_log_stats=True,
        enable_prefix_caching=True,
        enable_lora=True,
        max_lora_rank=32
    )

    tokenizer = llm.get_tokenizer()
    mclp = MultipleChoiceLogitsProcessor(tokenizer, choices=['Yes','No'])
    print("Model loaded successfully")

    print("\n[3/5] Creating prompts...")
    SYS_PROMPT = """
You are given a comment on reddit. Your task is to classify if it violates the given rule. Only respond Yes/No.
"""

    prompts = []
    for i, row in df_hard.iterrows():
        text = f"""
r/{row['subreddit']}
Rule: {row['rule']}

1) {row['positive_example_1']}
Violation: Yes

2) {row['positive_example_2']}
Violation: Yes

3) {row['negative_example_1']}
Violation: No

4) {row['negative_example_2']}
Violation: No

5) {row['body']}
"""

        messages = [
            {"role": "system", "content": SYS_PROMPT},
            {"role": "user", "content": text}
        ]

        prompt = tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=False,
        ) + "Answer:"
        prompts.append(prompt)

    print(f"Created {len(prompts)} prompts")

    print("\n[4/5] Running inference...")
    outputs = llm.generate(
        prompts,
        vllm.SamplingParams(
            skip_special_tokens=True,
            max_tokens=1,
            logits_processors=[mclp],
            logprobs=2,
        ),
        use_tqdm=True,
        lora_request=LoRARequest("default", 1, LORA_PATH)
    )
    print(f"Generated {len(outputs)} outputs")

    print("\n[5/5] Processing results...")
    logprobs = [
        {lp.decoded_token: lp.logprob for lp in out.outputs[0].logprobs[0].values()}
        for out in outputs
    ]

    logit_matrix = pd.DataFrame(logprobs)[['Yes','No']]
    qwen_probs = logit_matrix.apply(lambda x: softmax(x.values), axis=1, result_type="expand")
    qwen_probs.columns = ['Yes', 'No']
    qwen_probs['qwen_prob'] = qwen_probs['Yes']

    df_hard['qwen_prob'] = qwen_probs['qwen_prob'].values

    df_hard.to_csv('hard_examples_with_qwen.csv', index=False)
    print(f"\nSaved results to hard_examples_with_qwen.csv")
    print(f"Qwen prob stats:")
    print(qwen_probs['qwen_prob'].describe())

    print("\n" + "=" * 80)
    print("Qwen 14B Inference Complete!")
    print("=" * 80)

if __name__ == "__main__":
    main()
