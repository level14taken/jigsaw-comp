import pandas as pd
import numpy as np

# Load data
print("Loading data...")
wise_df = pd.read_csv('violation_sampling_csv.txt')
reddit_df = pd.read_csv('reddit-removal-log.csv')

print(f"Wise entries: {len(wise_df)}")
print(f"Reddit comments: {len(reddit_df)}")

# Normalize subreddit names
reddit_df['subreddit_lower'] = reddit_df['subreddit'].str.lower()
wise_df['subreddit_lower'] = wise_df['subreddit'].str.lower()

# Priority order
priority_order = {'PRIMARY': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
wise_df['priority_num'] = wise_df['priority'].map(priority_order)
wise_df = wise_df.sort_values('priority_num')

# Process each wise entry
results = []

for idx, row in wise_df.iterrows():
    rule = row['rule']
    subreddit = row['subreddit_lower']
    priority = row['priority']
    confidence = row['confidence']

    print(f"\n{'='*80}")
    print(f"Entry {idx+1}/{len(wise_df)}: Rule={rule}, Subreddit={subreddit}")
    print(f"Priority={priority}, Expected Confidence={confidence}")
    print('='*80)

    # Get comments from this subreddit
    subreddit_comments = reddit_df[reddit_df['subreddit_lower'] == subreddit]

    print(f"Total comments in {subreddit}: {len(subreddit_comments)}")

    if len(subreddit_comments) == 0:
        print("No comments found. Skipping.")
        results.append({
            'rule': rule,
            'subreddit': subreddit,
            'priority': priority,
            'expected_confidence': confidence,
            'total_available': 0,
            'sampled': 0,
            'violations': 0,
            'violation_prob': 0.0
        })
        continue

    # Sample 100 (or all if less than 100)
    sample_size = min(100, len(subreddit_comments))
    sampled = subreddit_comments.sample(n=sample_size, random_state=42)

    print(f"Sampled {sample_size} comments")
    print("\n--- COMMENTS TO REVIEW ---")

    # Display comments for manual review
    for i, (_, comment_row) in enumerate(sampled.iterrows(), 1):
        body = comment_row['body']
        print(f"\n[{i}/{sample_size}] {body[:200]}{'...' if len(body) > 200 else ''}")

    # Manual input for violations
    print(f"\n\nHow many of these {sample_size} comments violate the '{rule}' rule?")
    violations = int(input("Enter number of violations: "))

    violation_prob = violations / sample_size

    results.append({
        'rule': rule,
        'subreddit': subreddit,
        'priority': priority,
        'expected_confidence': confidence,
        'total_available': len(subreddit_comments),
        'sampled': sample_size,
        'violations': violations,
        'violation_prob': violation_prob
    })

    print(f"\nViolation probability: {violation_prob:.2%}")

# Create results dataframe
results_df = pd.DataFrame(results)
results_df.to_csv('wise_validation_results.csv', index=False)

print("\n\n" + "="*80)
print("FINAL RESULTS")
print("="*80)
print(results_df.to_string())

print("\n\nResults saved to: wise_validation_results.csv")
