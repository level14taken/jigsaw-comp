import os
os.environ["VLLM_USE_V1"] = "0"

import vllm
import torch
import pandas as pd
from logits_processor_zoo.vllm import MultipleChoiceLogitsProcessor
from vllm.lora.request import LoRARequest
from sentence_transformers import SentenceTransformer
from utils import build_dataset, build_labeled_corpus, get_semantic_examples
from constants import (
    BASE_MODEL_PATH, LORA_PATH, DATA_PATH, POSITIVE_ANSWER, NEGATIVE_ANSWER,
    EMBEDDING_MODEL_PATH
)
import multiprocessing as mp


def prepare_test_data_with_semantic_examples(df_slice):
    """Prepare test data with semantically selected examples"""
    # Build corpus for semantic search
    corpus_df = build_labeled_corpus(DATA_PATH)

    # Load embedding model
    embedding_model = SentenceTransformer(EMBEDDING_MODEL_PATH, device="cuda" if torch.cuda.is_available() else "cpu")

    results = []
    for _, row in df_slice.iterrows():
        pos_example, neg_example = get_semantic_examples(
            row["body"], row["rule"], row["subreddit"], corpus_df, embedding_model
        )

        row_dict = row.to_dict()
        row_dict["positive_example"] = pos_example
        row_dict["negative_example"] = neg_example
        results.append(row_dict)

    return pd.DataFrame(results)


def run_inference_on_device(df_slice):
    """Run vLLM inference on current process visible GPU"""
    llm = vllm.LLM(
        BASE_MODEL_PATH,
        quantization="gptq",
        tensor_parallel_size=1,
        gpu_memory_utilization=0.98,
        trust_remote_code=True,
        dtype="half",
        enforce_eager=True,
        max_model_len=2836,
        disable_log_stats=True,
        enable_prefix_caching=True,
        enable_lora=True,
        max_lora_rank=64,
    )

    tokenizer = llm.get_tokenizer()
    mclp = MultipleChoiceLogitsProcessor(tokenizer, choices=[POSITIVE_ANSWER, NEGATIVE_ANSWER])

    # Prepare data with semantic examples
    df_with_examples = prepare_test_data_with_semantic_examples(df_slice)
    test_dataset = build_dataset(df_with_examples)
    texts = test_dataset["prompt"]

    outputs = llm.generate(
        texts,
        vllm.SamplingParams(
            skip_special_tokens=True,
            max_tokens=1,
            logits_processors=[mclp],
            logprobs=2,
        ),
        use_tqdm=True,
        lora_request=LoRARequest("default", 1, LORA_PATH)
    )

    log_probs = [
        {lp.decoded_token: lp.logprob for lp in out.outputs[0].logprobs[0].values()}
        for out in outputs
    ]
    predictions = pd.DataFrame(log_probs)[[POSITIVE_ANSWER, NEGATIVE_ANSWER]]
    predictions["row_id"] = df_slice["row_id"].values
    return predictions


def worker(device_id, df_slice, return_dict):
    # Limit process to single GPU
    os.environ["CUDA_VISIBLE_DEVICES"] = str(device_id)
    print(f"[Worker {device_id}] Running on GPU {device_id}, data size={len(df_slice)}")

    preds = run_inference_on_device(df_slice)
    return_dict[device_id] = preds


def main():
    test_dataframe = pd.read_csv(f"{DATA_PATH}/test.csv")

    # Split data for parallel processing
    mid = len(test_dataframe) // 2
    df0 = test_dataframe.iloc[:mid].reset_index(drop=True)
    df1 = test_dataframe.iloc[mid:].reset_index(drop=True)

    manager = mp.Manager()
    return_dict = manager.dict()

    # Run parallel inference
    p0 = mp.Process(target=worker, args=(0, df0, return_dict))
    p1 = mp.Process(target=worker, args=(1, df1, return_dict))
    p0.start()
    p1.start()
    p0.join()
    p1.join()

    # Combine results
    predictions = pd.concat([return_dict[0], return_dict[1]], ignore_index=True)

    # Build submission
    submission = predictions[["row_id", POSITIVE_ANSWER]].rename(columns={POSITIVE_ANSWER: "rule_violation"})
    rq = submission['rule_violation'].rank(method='average') / (len(submission) + 1)
    submission['rule_violation'] = rq

    submission.to_csv("submission_semantic.csv", index=False)
    print("✅ Saved submission_semantic.csv")


if __name__ == "__main__":
    main()