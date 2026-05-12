import pandas as pd
import os

os.makedirs('round7_samples', exist_ok=True)

reddit_df = pd.read_csv('reddit-removal-log.csv')
reddit_df['subreddit_lower'] = reddit_df['subreddit'].str.lower()

# Round 7: Test the GIANTS - The_Donald, politics, AskReddit
subreddit_rules = [
    # THE_DONALD (184K comments) - UNTESTED for all rules
    ('the_donald', ['advertising', 'illegal_activity', 'medical_advice', 'financial_advice', 'legal_advice']),

    # POLITICS (147K comments) - Missing 3 rules
    ('politics', ['medical_advice', 'financial_advice', 'legal_advice']),

    # ASKREDDIT (110K comments) - Missing 2 rules
    ('askreddit', ['advertising', 'illegal_activity']),
]

created = 0
for subreddit, rules in subreddit_rules:
    comments = reddit_df[reddit_df['subreddit_lower'] == subreddit]

    if len(comments) == 0:
        print(f"WARNING: No comments found for {subreddit}")
        continue

    sample_size = min(100, len(comments))
    sampled = comments.sample(n=sample_size, random_state=42)

    for rule in rules:
        filename = f"round7_samples/{rule}_{subreddit}.csv"
        sampled[['body', 'subreddit']].to_csv(filename, index=False)
        created += 1
        print(f"Created: {filename} ({sample_size} comments)")

print(f"\n{'='*60}")
print(f"ROUND 7 SAMPLE PREPARATION COMPLETE")
print(f"{'='*60}")
print(f"Total files created: {created}")
print(f"Expected: 10 files")
print(f"\nTesting the GIANTS:")
print(f"  - The_Donald (184K comments): 5 rules")
print(f"  - politics (147K comments): 3 rules")
print(f"  - askreddit (110K comments): 2 rules")
