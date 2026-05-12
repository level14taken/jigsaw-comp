import pandas as pd

from trl import SFTTrainer, SFTConfig
from peft import LoraConfig
from tqdm.auto import tqdm
from transformers.utils import is_torch_bf16_gpu_available
from utils import build_dataset, get_dataframe_to_train
from constants import DATA_PATH, BASE_MODEL_PATH, LORA_PATH


def main():
    dataframe = get_dataframe_to_train(DATA_PATH)
    train_dataset = build_dataset(dataframe)

    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        lora_dropout=0.1,
        bias="none",
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        task_type="CAUSAL_LM",
    )

    training_args = SFTConfig(
        num_train_epochs=1,

        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,

        optim="paged_adamw_8bit",
        learning_rate=1e-4, #keep high, lora usually likes high.
        weight_decay=0.01,
        max_grad_norm=1.0,

        lr_scheduler_type="cosine",
        warmup_ratio=0.03,

        bf16=is_torch_bf16_gpu_available(),
        fp16=not is_torch_bf16_gpu_available(),
        dataloader_pin_memory=True,

        gradient_checkpointing=True,
        gradient_checkpointing_kwargs={"use_reentrant": False},

        save_strategy="no",
        report_to="none",

        completion_only_loss=True,
        packing=False,
        remove_unused_columns=False,
    )

    trainer = SFTTrainer(
        BASE_MODEL_PATH,
        args=training_args,
        train_dataset=train_dataset,
        peft_config=lora_config,
    )

    trainer.train()
    trainer.save_model(LORA_PATH)


if __name__ == "__main__":
    main()