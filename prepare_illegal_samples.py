import pandas as pd
import os

os.makedirs('illegal_samples', exist_ok=True)

reddit_df = pd.read_csv('reddit-removal-log.csv')
reddit_df['subreddit_lower'] = reddit_df['subreddit'].str.lower()

subreddits = [
    'syriancivilwar',
    'suicidewatch',
    'depression',
    'conspiracy',
    'latestagecapitalism',
    'socialism',
    'shitredditsays'
]

for subreddit in subreddits:
    comments = reddit_df[reddit_df['subreddit_lower'] == subreddit]

    if len(comments) > 0:
        sample_size = min(100, len(comments))
        sampled = comments.sample(n=sample_size, random_state=42)

        filename = f"illegal_samples/illegal_activity_{subreddit}.csv"
        sampled[['body', 'subreddit']].to_csv(filename, index=False)
        print(f"Saved {sample_size} comments from {subreddit}")
    else:
        print(f"No comments found for {subreddit}")

print("\nAll samples prepared in ./illegal_samples/")
