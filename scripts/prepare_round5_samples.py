import pandas as pd
import os

os.makedirs('round5_samples', exist_ok=True)

reddit_df = pd.read_csv('reddit-removal-log.csv')
reddit_df['subreddit_lower'] = reddit_df['subreddit'].str.lower()

subreddit_rules = [
    # SPOILERS - 7 tests
    ('pokemon', ['spoilers']),
    ('overwatch', ['spoilers']),
    ('wow', ['spoilers']),
    ('destinythegame', ['spoilers']),
    ('hearthstone', ['spoilers']),
    ('nba', ['spoilers']),
    ('fantasyfootball', ['spoilers']),

    # FINANCIAL_ADVICE - 5 tests
    ('fantasyfootball', ['financial_advice']),
    ('changemyview', ['financial_advice']),
    ('india', ['financial_advice']),
    ('canada', ['financial_advice']),
    ('christianity', ['financial_advice']),

    # LEGAL_ADVICE - 5 tests
    ('subredditdrama', ['legal_advice']),
    ('creepypms', ['legal_advice']),
    ('changemyview', ['legal_advice']),
    ('politicaldiscussion', ['legal_advice']),
    ('asktrumpsupporters', ['legal_advice']),
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
        filename = f"round5_samples/{rule}_{subreddit}.csv"
        sampled[['body', 'subreddit']].to_csv(filename, index=False)
        created += 1
        print(f"Created: {filename} ({sample_size} comments)")

print(f"\n{'='*60}")
print(f"ROUND 5 SAMPLE PREPARATION COMPLETE")
print(f"{'='*60}")
print(f"Total files created: {created}")
print(f"Expected: 17 files (7 spoilers + 5 financial + 5 legal)")
