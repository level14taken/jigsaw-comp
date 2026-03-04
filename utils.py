import pandas as pd
import torch
import numpy as np
from datasets import Dataset
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import semantic_search, dot_score
from tqdm.auto import tqdm
from constants import (
    POSITIVE_ANSWER, NEGATIVE_ANSWER, COMPLETE_PHRASE, BASE_PROMPT,
    EMBEDDING_MODEL_PATH, EMBEDDING_MODEL_QUERY, TOP_K_SEMANTIC, EMBEDDING_BATCH_SIZE
)
import random
random.seed(42)
np.random.seed(42)


def build_prompt(row):
    return f"""
{BASE_PROMPT}

Subreddit: r/{row["subreddit"]}
Rule: {row["rule"]}
Examples:
1) {row["positive_example"]}
{COMPLETE_PHRASE} Yes

2) {row["negative_example"]}
{COMPLETE_PHRASE} No

---
Comment: {row["body"]}
{COMPLETE_PHRASE}"""


def build_labeled_corpus(data_path):
    """Build comprehensive labeled corpus from all available data"""
    train_dataset = pd.read_csv(f"{data_path}/train.csv")
    test_dataset = pd.read_csv(f"{data_path}/test.csv")

    corpus = []

    # Add train data
    for _, row in train_dataset.iterrows():
        corpus.append({
            "body": row["body"],
            "rule": row["rule"],
            "subreddit": row["subreddit"],
            "rule_violation": row["rule_violation"]
        })

    # Add positive examples from test data
    for _, row in test_dataset.iterrows():
        for i in [1, 2]:
            corpus.append({
                "body": row[f"positive_example_{i}"],
                "rule": row["rule"],
                "subreddit": row["subreddit"],
                "rule_violation": 1
            })

    # Add negative examples from test data
    for _, row in test_dataset.iterrows():
        for i in [1, 2]:
            corpus.append({
                "body": row[f"negative_example_{i}"],
                "rule": row["rule"],
                "subreddit": row["subreddit"],
                "rule_violation": 0
            })

    corpus_df = pd.DataFrame(corpus).drop_duplicates().reset_index(drop=True)
    corpus_df["corpus_id"] = corpus_df.index
    return corpus_df


def get_semantic_examples(target_comment, target_rule, target_subreddit, corpus_df, embedding_model):
    """Find semantically similar positive and negative examples, avoiding exact matches"""

    # Filter corpus by rule and subreddit
    rule_corpus = corpus_df[
        (corpus_df["rule"] == target_rule) &
        (corpus_df["subreddit"] == target_subreddit) &
        (corpus_df["body"] != target_comment)  # Avoid exact matches for leakage prevention
    ].reset_index(drop=True)

    if len(rule_corpus) == 0:
        # Fallback to any rule if no matches in same rule/subreddit
        rule_corpus = corpus_df[corpus_df["body"] != target_comment].reset_index(drop=True)

    # Encode target comment
    target_embedding = embedding_model.encode(
        [target_comment],
        prompt=EMBEDDING_MODEL_QUERY,
        batch_size=1,
        convert_to_tensor=True,
        normalize_embeddings=True,
    )

    # Encode corpus
    corpus_embeddings = embedding_model.encode(
        rule_corpus["body"].tolist(),
        batch_size=EMBEDDING_BATCH_SIZE,
        convert_to_tensor=True,
        normalize_embeddings=True,
        show_progress_bar=False,
    )

    # Find most similar examples
    search_results = semantic_search(
        target_embedding,
        corpus_embeddings,
        top_k=min(TOP_K_SEMANTIC, len(rule_corpus)),
        score_function=dot_score,
    )[0]

    # Get positive and negative examples separately
    positive_examples = []
    negative_examples = []

    for result in search_results:
        corpus_idx = result["corpus_id"]
        example_row = rule_corpus.iloc[corpus_idx]

        if example_row["rule_violation"] == 1 and len(positive_examples) == 0:
            positive_examples.append(example_row["body"])
        elif example_row["rule_violation"] == 0 and len(negative_examples) == 0:
            negative_examples.append(example_row["body"])

        # Stop when we have both types
        if len(positive_examples) > 0 and len(negative_examples) > 0:
            break

    # Fallback to random if semantic search fails
    if len(positive_examples) == 0:
        pos_candidates = rule_corpus[rule_corpus["rule_violation"] == 1]
        if len(pos_candidates) > 0:
            positive_examples.append(pos_candidates.sample(1)["body"].iloc[0])

    if len(negative_examples) == 0:
        neg_candidates = rule_corpus[rule_corpus["rule_violation"] == 0]
        if len(neg_candidates) > 0:
            negative_examples.append(neg_candidates.sample(1)["body"].iloc[0])

    return (
        positive_examples[0] if positive_examples else "No positive example found",
        negative_examples[0] if negative_examples else "No negative example found"
    )


def get_dataframe_to_train(data_path):
    """Get training dataframe with semantically selected examples"""
    train_dataset = pd.read_csv(f"{data_path}/train.csv")
    test_dataset = pd.read_csv(f"{data_path}/test.csv").sample(frac=0.5, random_state=42).reset_index(drop=True)

    # Build corpus for semantic search
    corpus_df = build_labeled_corpus(data_path)

    # Load embedding model
    print("Loading embedding model for semantic example selection...")
    embedding_model = SentenceTransformer(EMBEDDING_MODEL_PATH, device="cuda" if torch.cuda.is_available() else "cpu")

    flatten = []

    # Process training data with semantic example selection
    print("Processing training data with semantic examples...")
    train_semantic = []
    for _, row in tqdm(train_dataset.iterrows(), total=len(train_dataset), desc="Train semantic selection"):
        pos_example, neg_example = get_semantic_examples(
            row["body"], row["rule"], row["subreddit"], corpus_df, embedding_model
        )
        train_row = {
            "body": row["body"],
            "rule": row["rule"],
            "subreddit": row["subreddit"],
            "rule_violation": row["rule_violation"],
            "positive_example": pos_example,
            "negative_example": neg_example
        }
        train_semantic.append(train_row)

    flatten.append(pd.DataFrame(train_semantic))

    # Process test data examples with semantic selection
    for violation_type in ["positive", "negative"]:
        for i in range(1, 3):
            print(f"Processing {violation_type}_example_{i} with semantic selection...")
            test_semantic = []

            for _, row in tqdm(test_dataset.iterrows(), total=len(test_dataset), desc=f"{violation_type}_{i}"):
                target_body = row[f"{violation_type}_example_{i}"]
                pos_example, neg_example = get_semantic_examples(
                    target_body, row["rule"], row["subreddit"], corpus_df, embedding_model
                )

                test_row = {
                    "body": target_body,
                    "rule": row["rule"],
                    "subreddit": row["subreddit"],
                    "rule_violation": 1 if violation_type == "positive" else 0,
                    "positive_example": pos_example,
                    "negative_example": neg_example
                }
                test_semantic.append(test_row)

            flatten.append(pd.DataFrame(test_semantic))

    # Combine all data
    dataframe = pd.concat(flatten, axis=0, ignore_index=True)
    dataframe = dataframe.drop_duplicates(ignore_index=True)

    return dataframe


def build_dataset(dataframe):
    """Build dataset for training"""
    dataframe["prompt"] = dataframe.apply(build_prompt, axis=1)

    columns = ["prompt"]
    if "rule_violation" in dataframe:
        dataframe["completion"] = dataframe["rule_violation"].map(
            {
                1: POSITIVE_ANSWER,
                0: NEGATIVE_ANSWER,
            }
        )
        columns.append("completion")

    dataframe = dataframe[columns]
    dataset = Dataset.from_pandas(dataframe)
    dataset.to_pandas().to_csv("/kaggle/working/dataset.csv", index=False)
    return dataset