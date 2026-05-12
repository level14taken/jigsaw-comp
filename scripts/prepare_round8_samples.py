import pandas as pd
import os

os.makedirs('round8_samples', exist_ok=True)

reddit_df = pd.read_csv('reddit-removal-log.csv')
reddit_df['subreddit_lower'] = reddit_df['subreddit'].str.lower()

# Round 8: Smart testing - only test rules that make sense

subreddit_rules = [
    # TWOXCHROMOSOMES (51K) - Women's issues
    # Good for: advertising (MLM/beauty spam), illegal_activity (harassment/abuse), legal_advice (domestic violence, workplace)
    ('twoxchromosomes', ['advertising', 'illegal_activity', 'legal_advice']),

    # SEX (12K) - Sexuality discussions
    # Good for: advertising (sex toys, porn sites), illegal_activity (revenge porn, exploitation), legal_advice (consent, age of consent)
    ('sex', ['advertising', 'illegal_activity', 'legal_advice']),

    # ASKWOMEN (13K) - Women Q&A
    # Good for: advertising, illegal_activity, legal_advice (similar to TwoX)
    ('askwomen', ['advertising', 'illegal_activity', 'legal_advice']),

    # FANTASYFOOTBALL (8K) - Fantasy sports
    # Good for: advertising (betting sites, DFS platforms), illegal_activity (gambling advice)
    ('fantasyfootball', ['advertising', 'illegal_activity']),
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
        filename = f"round8_samples/{rule}_{subreddit}.csv"
        sampled[['body', 'subreddit']].to_csv(filename, index=False)
        created += 1
        print(f"Created: {filename} ({sample_size} comments)")

print(f"\n{'='*60}")
print(f"ROUND 8 SAMPLE PREPARATION COMPLETE")
print(f"{'='*60}")
print(f"Total files created: {created}")
print(f"Expected: 11 files")
print(f"\nSmart testing strategy:")
print(f"  - TwoXChromosomes: advertising, illegal_activity, legal_advice")
print(f"  - sex: advertising, illegal_activity, legal_advice")
print(f"  - AskWomen: advertising, illegal_activity, legal_advice")
print(f"  - fantasyfootball: advertising, illegal_activity")
