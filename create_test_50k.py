import pandas as pd
import numpy as np

# Load unlabelled data for body content
unlabelled = pd.read_csv('/kaggle/input/jigsaw-unlabelled-14b/sampled_unlabelled_100k_with_predictions.csv')

print(f"Total unlabelled data: {len(unlabelled)}")

# 2 existing rules from train.csv (these will be PSEUDO rules - have pseudo data)
existing_rules = [
    "no advertising: spam, referral links, unsolicited advertising, and promotional content are not allowed.",
    "no legal advice: do not offer or request legal advice."
]

# 4 NEW rules that don't exist in train.csv (these will be NON-PSEUDO rules)
new_rules = [
    "no harassment: do not engage in personal attacks or harassment.",
    "no misinformation: do not spread false or misleading information.",
    "be respectful: treat all community members with respect and dignity.",
    "stay on topic: keep discussions relevant to the community purpose."
]

# Combine all 6 rules
all_rules = existing_rules + new_rules

# Sample 55k bodies from unlabelled data
sample_size = 55000
sampled_bodies = unlabelled['body'].sample(n=min(sample_size, len(unlabelled)),
                                           replace=(sample_size > len(unlabelled)),
                                           random_state=42).reset_index(drop=True)

# Distribute rules equally across 55k rows
samples_per_rule = sample_size // len(all_rules)  # 9166 per rule
rules_list = []

for i, rule in enumerate(all_rules):
    start_idx = i * samples_per_rule
    end_idx = (i + 1) * samples_per_rule if i < len(all_rules) - 1 else sample_size
    rules_list.extend([rule] * (end_idx - start_idx))

print(f"\nSamples per rule: ~{samples_per_rule}")
print(f"Total samples: {len(rules_list)}")

# Create new test dataframe
new_test_df = pd.DataFrame({
    'id': range(sample_size),
    'rule': rules_list,
    'body': sampled_bodies[:sample_size]
})

# Shuffle
new_test_df = new_test_df.sample(frac=1, random_state=42).reset_index(drop=True)
new_test_df['id'] = range(len(new_test_df))

print(f"\nFinal test.csv shape: {new_test_df.shape}")
print(f"\nRule distribution in new test.csv:")
print(new_test_df['rule'].value_counts().sort_index())
print(f"\n2 PSEUDO rules (existing in train.csv):")
for r in existing_rules:
    count = len(new_test_df[new_test_df['rule'] == r])
    print(f"  {r[:60]}... : {count} rows")
print(f"\n4 NON-PSEUDO rules (new, not in train.csv):")
for r in new_rules:
    count = len(new_test_df[new_test_df['rule'] == r])
    print(f"  {r[:60]}... : {count} rows")

new_test_df.to_csv('test_55k.csv', index=False)
print(f"\nSaved to test_55k.csv")
print(f"\nFirst few rows:")
print(new_test_df.head())
