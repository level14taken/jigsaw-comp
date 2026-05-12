import pandas as pd
import os

os.makedirs('round4_samples', exist_ok=True)

reddit_df = pd.read_csv('reddit-removal-log.csv')
reddit_df['subreddit_lower'] = reddit_df['subreddit'].str.lower()

# Round 4: Missing high-volume subreddits
subreddit_rules = [
    ('news', ['illegal_activity']),
    ('pics', ['advertising']),
    ('mma', ['illegal_activity', 'spoilers']),
    ('funny', ['advertising']),
    ('gaming', ['advertising']),
    ('diy', ['financial_advice', 'advertising']),
    ('food', ['advertising', 'medical_advice']),
    ('nfl', ['spoilers']),
    ('cfb', ['spoilers']),
    ('sandersforpresident', ['illegal_activity']),
    ('europe', ['illegal_activity']),
    ('atheism', ['illegal_activity']),
]

for subreddit, rules in subreddit_rules:
    comments = reddit_df[reddit_df['subreddit_lower'] == subreddit]

    if len(comments) > 0:
        sample_size = min(100, len(comments))
        sampled = comments.sample(n=sample_size, random_state=42)

        for rule in rules:
            filename = f"round4_samples/{rule}_{subreddit}.csv"
            sampled[['body', 'subreddit']].to_csv(filename, index=False)
            print(f"Saved {sample_size} comments: {rule} @ {subreddit}")
    else:
        print(f"No comments found for {subreddit}")

print("\nAll round 4 samples prepared in ./round4_samples/")
