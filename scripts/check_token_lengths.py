import pandas as pd
import numpy as np
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-v3-base", use_fast=False)

train_df = pd.read_csv("/home/manoj/my_projects/jigsaw/train.csv")
reddit_df = pd.read_csv("/home/manoj/my_projects/jigsaw/reddit-removal-log.csv", nrows=10000)

with open("/home/manoj/my_projects/jigsaw/rules.txt", "r") as f:
    rules = [line.strip() for line in f.readlines()]

print("=== Rule Token Lengths ===")
for rule in rules:
    tokens = tokenizer.tokenize(rule)
    print(f"{len(tokens):3d} tokens: {rule[:60]}...")

print("\n=== Train Data Analysis ===")
train_lengths = []
for idx, row in train_df.iterrows():
    if pd.notna(row['body']) and pd.notna(row['rule']):
        text = f"{row['body']} [SEP] {row['rule']}"
        tokens = tokenizer.tokenize(text)
        train_lengths.append(len(tokens))

train_lengths = np.array(train_lengths)
print(f"Total samples: {len(train_lengths)}")
print(f"Min length: {train_lengths.min()}")
print(f"Max length: {train_lengths.max()}")
print(f"Mean length: {train_lengths.mean():.1f}")
print(f"Median length: {np.median(train_lengths):.1f}")
print(f"75th percentile: {np.percentile(train_lengths, 75):.1f}")
print(f"90th percentile: {np.percentile(train_lengths, 90):.1f}")
print(f"95th percentile: {np.percentile(train_lengths, 95):.1f}")
print(f"99th percentile: {np.percentile(train_lengths, 99):.1f}")
print(f"\nSamples > 128 tokens: {(train_lengths > 128).sum()} ({100*(train_lengths > 128).mean():.1f}%)")
print(f"Samples > 256 tokens: {(train_lengths > 256).sum()} ({100*(train_lengths > 256).mean():.1f}%)")
print(f"Samples > 512 tokens: {(train_lengths > 512).sum()} ({100*(train_lengths > 512).mean():.1f}%)")

print("\n=== Reddit Removal Log Sample Analysis (10k samples) ===")
reddit_lengths = []
for idx, row in reddit_df.iterrows():
    if pd.notna(row['body']):
        for rule in rules:
            text = f"{row['body']} [SEP] {rule}"
            tokens = tokenizer.tokenize(text)
            reddit_lengths.append(len(tokens))

reddit_lengths = np.array(reddit_lengths)
print(f"Total samples: {len(reddit_lengths)}")
print(f"Min length: {reddit_lengths.min()}")
print(f"Max length: {reddit_lengths.max()}")
print(f"Mean length: {reddit_lengths.mean():.1f}")
print(f"Median length: {np.median(reddit_lengths):.1f}")
print(f"75th percentile: {np.percentile(reddit_lengths, 75):.1f}")
print(f"90th percentile: {np.percentile(reddit_lengths, 90):.1f}")
print(f"95th percentile: {np.percentile(reddit_lengths, 95):.1f}")
print(f"99th percentile: {np.percentile(reddit_lengths, 99):.1f}")
print(f"\nSamples > 128 tokens: {(reddit_lengths > 128).sum()} ({100*(reddit_lengths > 128).mean():.1f}%)")
print(f"Samples > 256 tokens: {(reddit_lengths > 256).sum()} ({100*(reddit_lengths > 256).mean():.1f}%)")
print(f"Samples > 512 tokens: {(reddit_lengths > 512).sum()} ({100*(reddit_lengths > 512).mean():.1f}%)")
