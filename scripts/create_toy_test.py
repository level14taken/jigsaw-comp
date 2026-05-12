#!/usr/bin/env python3
"""Create toy test.csv with 55k rows mimicking real test dataset structure"""

import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Read train data
print("Reading train.csv...")
train_df = pd.read_csv('train.csv')
print(f"Train shape: {train_df.shape}")
print(f"Unique rules in train: {train_df['rule'].nunique()}")

# Get unique rules from train
train_rules = train_df['rule'].unique()
print(f"\nRules in train: {len(train_rules)}")

# Create 6 rules total (2 from train, 4 new ones)
selected_train_rules = train_rules[:2] if len(train_rules) >= 2 else train_rules

# Create 4 new rules not in train
new_rules = [
    "No Hate Speech: Racism, sexism, homophobia, and other forms of bigotry are not tolerated.",
    "No Personal Attacks: Attack the argument, not the person.",
    "Be Civil: Treat others with respect and engage in good faith.",
    "No Misinformation: Do not spread false or misleading information."
]

all_rules = list(selected_train_rules) + new_rules
print(f"\nSelected rules for test:")
for i, rule in enumerate(all_rules, 1):
    print(f"{i}. {rule[:80]}...")

# Create toy test dataset
print(f"\nCreating toy test.csv with 55k rows...")

rows = []
row_id = 0

# Distribute rows across 6 rules
rows_per_rule = 55000 // 6
remainder = 55000 % 6

for rule_idx, rule in enumerate(all_rules):
    # Calculate rows for this rule
    n_rows = rows_per_rule + (1 if rule_idx < remainder else 0)

    print(f"Generating {n_rows} rows for rule {rule_idx+1}...")

    # Get bodies from train (corrupt/shuffle them)
    all_bodies = train_df['body'].dropna().tolist()

    # Generate rows for this rule
    for i in range(n_rows):
        # Randomly pick a body and corrupt it slightly
        body = random.choice(all_bodies)

        # Add some noise to body to make it slightly different
        if random.random() < 0.3:
            noise_words = ["updated", "new", "2024", "check this", "interesting"]
            body = f"{random.choice(noise_words)} {body}"

        # Generate positive examples (compliant with rule)
        pos_ex_1 = random.choice(all_bodies)
        pos_ex_2 = random.choice(all_bodies)

        # Generate negative examples (violating rule)
        neg_ex_1 = random.choice(all_bodies)
        neg_ex_2 = random.choice(all_bodies)

        rows.append({
            'row_id': row_id,
            'body': body,
            'rule': rule,
            'positive_example_1': pos_ex_1,
            'positive_example_2': pos_ex_2,
            'negative_example_1': neg_ex_1,
            'negative_example_2': neg_ex_2
        })

        row_id += 1

# Create DataFrame
test_df = pd.DataFrame(rows)

print(f"\nToy test.csv created:")
print(f"Shape: {test_df.shape}")
print(f"Columns: {test_df.columns.tolist()}")
print(f"Rules: {test_df['rule'].nunique()}")
print(f"\nRule distribution:")
print(test_df['rule'].value_counts())

# Save to CSV
test_df.to_csv('toy_test.csv', index=False)
print(f"\nSaved to toy_test.csv")
print(f"File size: {test_df.memory_usage(deep=True).sum() / 1024 / 1024:.2f} MB")
