import pandas as pd
import os

os.makedirs('expansion_samples', exist_ok=True)

reddit_df = pd.read_csv('reddit-removal-log.csv')
reddit_df['subreddit_lower'] = reddit_df['subreddit'].str.lower()

# Define subreddit-rule mappings for expansion
subreddit_rules = [
    # Multi-rule subreddits
    ('relationships', ['financial_advice', 'medical_advice', 'legal_advice']),
    ('askreddit', ['financial_advice', 'medical_advice', 'legal_advice']),

    # Single-rule subreddits
    ('twoxchromosomes', ['medical_advice']),
    ('blackpeopletwitter', ['illegal_activity']),
    ('leagueoflegends', ['spoilers']),
    ('pokemongo', ['advertising']),
    ('pcmasterrace', ['advertising']),
    ('android', ['advertising']),
    ('movies', ['spoilers']),
    ('television', ['spoilers']),
]

for subreddit, rules in subreddit_rules:
    comments = reddit_df[reddit_df['subreddit_lower'] == subreddit]

    if len(comments) > 0:
        sample_size = min(100, len(comments))
        sampled = comments.sample(n=sample_size, random_state=42)

        # Create one sample file per rule for this subreddit
        for rule in rules:
            filename = f"expansion_samples/{rule}_{subreddit}.csv"
            sampled[['body', 'subreddit']].to_csv(filename, index=False)
            print(f"Saved {sample_size} comments: {rule} @ {subreddit}")
    else:
        print(f"No comments found for {subreddit}")

print("\nAll expansion samples prepared in ./expansion_samples/")
