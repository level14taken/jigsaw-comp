import pandas as pd
import os

results_dir = 'illegal_results'
results = []

# Read all result files
for filename in sorted(os.listdir(results_dir)):
    if filename.endswith('_result.txt'):
        filepath = os.path.join(results_dir, filename)
        with open(filepath, 'r') as f:
            lines = f.readlines()
            result = {}
            for line in lines:
                if ':' in line:
                    key, value = line.strip().split(':', 1)
                    result[key.strip()] = value.strip()
            results.append(result)

# Create dataframe
df = pd.DataFrame(results)
df['violations'] = df['violations'].astype(int)
df['violation_rate'] = df['violation_rate'].astype(float)
df['total_comments'] = df['total_comments'].astype(int)

# Sort by violation rate
df = df.sort_values('violation_rate', ascending=False)

# Save results
df.to_csv('illegal_activity_summary.csv', index=False)

print("="*80)
print("ILLEGAL ACTIVITY RULE - CORRECTED ANALYSIS")
print("Drug-related activity, Violence, Exploitation, Theft, Criminal Behavior")
print("="*80)
print(f"\nTotal subreddits tested: {len(df)}")
print(f"Total comments analyzed: {df['total_comments'].sum()}")
print(f"Total violations found: {df['violations'].sum()}")
print(f"Overall violation rate: {df['violations'].sum() / df['total_comments'].sum():.2%}")

print("\n" + "="*80)
print("RESULTS BY SUBREDDIT (sorted by violation rate)")
print("="*80)
print(f"\n{df[['subreddit', 'violations', 'violation_rate']].to_string(index=False)}")

print("\n" + "="*80)
print("TOP PERFORMERS")
print("="*80)
top3 = df.head(3)
for idx, row in top3.iterrows():
    print(f"\n{row['subreddit']}: {row['violation_rate']:.1%} ({row['violations']}/100)")

print("\n" + "="*80)
print("COMPARISON WITH PREVIOUS (INCORRECT) ANALYSIS")
print("="*80)
print("\nPrevious incorrect targets:")
print("  - soccerstreams: 94% (but this was PIRACY, not drugs/violence/exploitation)")
print("  - jailbreak: 15% (but this was SOFTWARE PIRACY, not relevant)")
print("\nCorrect targets for REAL illegal activity:")
for idx, row in df.head(3).iterrows():
    print(f"  - {row['subreddit']}: {row['violation_rate']:.1%}")

print(f"\n\nResults saved to: illegal_activity_summary.csv")
