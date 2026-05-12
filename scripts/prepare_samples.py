import pandas as pd
import os

# Create samples directory
os.makedirs('samples', exist_ok=True)

# Load data
print("Loading data...")
wise_df = pd.read_csv('violation_sampling_csv.txt')
reddit_df = pd.read_csv('reddit-removal-log.csv')

# Normalize subreddit names
reddit_df['subreddit_lower'] = reddit_df['subreddit'].str.lower()
wise_df['subreddit_lower'] = wise_df['subreddit'].str.lower()

# Process each wise entry
for idx, row in wise_df.iterrows():
    rule = row['rule']
    subreddit = row['subreddit_lower']
    priority = row['priority']
    confidence = row['confidence']

    # Get comments from this subreddit
    subreddit_comments = reddit_df[reddit_df['subreddit_lower'] == subreddit]

    if len(subreddit_comments) > 0:
        # Sample 100 (or all if less than 100)
        sample_size = min(100, len(subreddit_comments))
        sampled = subreddit_comments.sample(n=sample_size, random_state=42)

        # Save sample
        filename = f"samples/{rule}_{subreddit}_{priority}.csv"
        sampled[['body', 'subreddit']].to_csv(filename, index=False)
        print(f"Saved {sample_size} comments to {filename}")
    else:
        print(f"No comments for {rule} in {subreddit}")

print("\nAll samples prepared in ./samples/ directory")
