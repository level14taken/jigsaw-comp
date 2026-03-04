import pandas as pd
import os

os.makedirs('round6_samples', exist_ok=True)

reddit_df = pd.read_csv('reddit-removal-log.csv')
reddit_df['subreddit_lower'] = reddit_df['subreddit'].str.lower()

subreddit_rules = [
    # FINANCIAL_ADVICE - 8 tests
    ('iama', ['financial_advice']),
    ('getmotivated', ['financial_advice']),
    ('lifeprotips', ['financial_advice']),
    ('technology', ['financial_advice']),
    ('tifu', ['financial_advice']),
    ('askhistorians', ['financial_advice']),
    ('space', ['financial_advice']),
    ('philosophy', ['financial_advice']),

    # LEGAL_ADVICE - 8 tests
    ('enoughtrumpspam', ['legal_advice']),
    ('neutralpolitics', ['legal_advice']),
    ('canadapolitics', ['legal_advice']),
    ('askhistorians', ['legal_advice']),
    ('europe', ['legal_advice']),
    ('history', ['legal_advice']),
    ('purplepilldebate', ['legal_advice']),
    ('shitredditsays', ['legal_advice']),
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
        filename = f"round6_samples/{rule}_{subreddit}.csv"
        sampled[['body', 'subreddit']].to_csv(filename, index=False)
        created += 1
        print(f"Created: {filename} ({sample_size} comments)")

print(f"\n{'='*60}")
print(f"ROUND 6 SAMPLE PREPARATION COMPLETE")
print(f"{'='*60}")
print(f"Total files created: {created}")
print(f"Expected: 16 files (8 financial + 8 legal)")
print(f"\nFOCUS: Finding more financial_advice and legal_advice violations")
