import pandas as pd
import os

results_dir = 'round6_results'
results = []

# Read all round 6 result files
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

# Sort by rule then by violation rate
df = df.sort_values(['rule', 'violation_rate'], ascending=[True, False])

# Save results
df.to_csv('round6_summary.csv', index=False)

print("="*80)
print("ROUND 6 ANALYSIS RESULTS - FINANCIAL & LEGAL ADVICE FOCUS")
print("="*80)
print(f"\nTotal subreddit-rule combinations tested: {len(df)}")
print(f"Total comments analyzed: {df['total_comments'].sum()}")
print(f"Total violations found: {df['violations'].sum()}")
print(f"Overall violation rate: {df['violations'].sum() / df['total_comments'].sum():.2%}")

# Group by rule
print("\n" + "="*80)
print("RESULTS BY RULE")
print("="*80)
for rule in df['rule'].unique():
    rule_df = df[df['rule'] == rule]
    print(f"\n{rule.upper().replace('_', ' ')}:")
    print(f"{rule_df[['subreddit', 'violations', 'violation_rate']].to_string(index=False)}")
    print(f"  Total: {rule_df['violations'].sum()}/{rule_df['total_comments'].sum()} ({rule_df['violations'].sum()/rule_df['total_comments'].sum():.1%})")

# Find new valuable sources
print("\n" + "="*80)
print("NEW HIGH-VALUE SOURCES (≥3% violation rate)")
print("="*80)
high_value = df[df['violation_rate'] >= 3.0].sort_values('violation_rate', ascending=False)
if len(high_value) > 0:
    print(high_value[['rule', 'subreddit', 'violations', 'violation_rate']].to_string(index=False))
else:
    print("⚠️  None found with ≥3% rate")

# Borderline sources
print("\n" + "="*80)
print("BORDERLINE SOURCES (1-2% violation rate)")
print("="*80)
borderline = df[(df['violation_rate'] >= 1.0) & (df['violation_rate'] < 3.0)].sort_values('violation_rate', ascending=False)
if len(borderline) > 0:
    print(borderline[['rule', 'subreddit', 'violations', 'violation_rate']].to_string(index=False))
else:
    print("None found")

# Failed predictions
print("\n" + "="*80)
print("FAILED PREDICTIONS (0% violations)")
print("="*80)
zeros = df[df['violation_rate'] == 0]
for _, row in zeros.iterrows():
    print(f"  - {row['rule']} @ {row['subreddit']}")

print(f"\n\nResults saved to: round6_summary.csv")
