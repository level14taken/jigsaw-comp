import pandas as pd
import os

os.makedirs('round9_samples', exist_ok=True)

reddit_df = pd.read_csv('reddit-removal-log.csv')
reddit_df['subreddit_lower'] = reddit_df['subreddit'].str.lower()

# Round 9: Financial advice in women's subreddits
subreddit_rules = [
    ('twoxchromosomes', ['financial_advice']),
    ('askwomen', ['financial_advice']),
    ('sex', ['financial_advice']),
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
        filename = f"round9_samples/{rule}_{subreddit}.csv"
        sampled[['body', 'subreddit']].to_csv(filename, index=False)
        created += 1
        print(f"Created: {filename} ({sample_size} comments)")

print(f"\n{'='*60}")
print(f"ROUND 9 SAMPLE PREPARATION COMPLETE")
print(f"{'='*60}")
print(f"Total files created: {created}")
print(f"Expected: 3 files")
print(f"\nTesting financial_advice in women's subreddits:")
print(f"  - TwoXChromosomes (51K comments)")
print(f"  - AskWomen (13K comments)")
print(f"  - sex (12K comments)")
