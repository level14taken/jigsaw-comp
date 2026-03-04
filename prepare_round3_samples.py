import pandas as pd
import os

os.makedirs('round3_samples', exist_ok=True)

reddit_df = pd.read_csv('reddit-removal-log.csv')
reddit_df['subreddit_lower'] = reddit_df['subreddit'].str.lower()

# Round 3: New high-potential subreddits
subreddit_rules = [
    ('gonewild', ['advertising']),
    ('explainlikeimfive', ['financial_advice', 'medical_advice', 'legal_advice']),
    ('politics', ['illegal_activity', 'advertising']),
    ('science', ['medical_advice']),
    ('askscience', ['medical_advice']),
    ('worldnews', ['illegal_activity']),
    ('games', ['spoilers', 'advertising']),
    ('futurology', ['advertising', 'financial_advice']),
    ('videos', ['advertising']),
    ('hillaryclinton', ['illegal_activity']),
]

for subreddit, rules in subreddit_rules:
    comments = reddit_df[reddit_df['subreddit_lower'] == subreddit]

    if len(comments) > 0:
        sample_size = min(100, len(comments))
        sampled = comments.sample(n=sample_size, random_state=42)

        for rule in rules:
            filename = f"round3_samples/{rule}_{subreddit}.csv"
            sampled[['body', 'subreddit']].to_csv(filename, index=False)
            print(f"Saved {sample_size} comments: {rule} @ {subreddit}")
    else:
        print(f"No comments found for {subreddit}")

print("\nAll round 3 samples prepared in ./round3_samples/")
