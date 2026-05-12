import pandas as pd
import os

results_dir = 'round7_results'
results = []

# Read all round 7 result files
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

# Sort by subreddit then by violation rate
df = df.sort_values(['subreddit', 'violation_rate'], ascending=[True, False])

# Save results
df.to_csv('round7_summary.csv', index=False)

print("="*80)
print("ROUND 7 ANALYSIS RESULTS - TESTING THE GIANTS")
print("="*80)
print(f"\nTotal subreddit-rule combinations tested: {len(df)}")
print(f"Total comments analyzed: {df['total_comments'].sum()}")
print(f"Total violations found: {df['violations'].sum()}")
print(f"Overall violation rate: {df['violations'].sum() / df['total_comments'].sum():.2%}")

# Group by subreddit
print("\n" + "="*80)
print("RESULTS BY SUBREDDIT")
print("="*80)
for subreddit in df['subreddit'].unique():
    sub_df = df[df['subreddit'] == subreddit]
    print(f"\n{subreddit.upper()} ({sub_df['total_comments'].sum()} comments tested):")
    print(f"{sub_df[['rule', 'violations', 'violation_rate']].to_string(index=False)}")
    print(f"  Total: {sub_df['violations'].sum()}/{sub_df['total_comments'].sum()} ({sub_df['violations'].sum()/sub_df['total_comments'].sum():.1%})")

# Find ANY sources ≥3%
print("\n" + "="*80)
print("HIGH-VALUE SOURCES (≥3% violation rate)")
print("="*80)
high_value = df[df['violation_rate'] >= 3.0].sort_values('violation_rate', ascending=False)
if len(high_value) > 0:
    print(high_value[['rule', 'subreddit', 'violations', 'violation_rate']].to_string(index=False))
else:
    print("⚠️  None found with ≥3% rate")

# Show ALL non-zero results
print("\n" + "="*80)
print("ALL NON-ZERO RESULTS")
print("="*80)
non_zero = df[df['violation_rate'] > 0].sort_values('violation_rate', ascending=False)
if len(non_zero) > 0:
    print(non_zero[['rule', 'subreddit', 'violations', 'violation_rate']].to_string(index=False))
else:
    print("⚠️  NO violations found in any combination!")

# Failed predictions
print("\n" + "="*80)
print("ZERO VIOLATIONS (0%)")
print("="*80)
zeros = df[df['violation_rate'] == 0]
for _, row in zeros.iterrows():
    print(f"  - {row['rule']} @ {row['subreddit']}")

print(f"\n\nResults saved to: round7_summary.csv")
