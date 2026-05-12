import pandas as pd
import os

results_dir = 'results'
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

# Merge with expected confidence from wise file
wise_df = pd.read_csv('violation_sampling_csv.txt')
wise_df['subreddit'] = wise_df['subreddit'].str.lower()

df = df.merge(
    wise_df[['rule', 'subreddit', 'confidence']],
    on=['rule', 'subreddit'],
    how='left'
)
df.rename(columns={'confidence': 'expected_confidence'}, inplace=True)

# Sort by priority
priority_order = {'PRIMARY': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
df['priority_num'] = df['priority'].map(priority_order)
df = df.sort_values('priority_num')

# Save full results
df.to_csv('wise_validation_summary.csv', index=False)

print("="*80)
print("WISE HYPOTHESIS VALIDATION RESULTS")
print("="*80)
print(f"\nTotal hypotheses tested: {len(df)}")
print(f"Total comments analyzed: {df['total_comments'].sum()}")
print(f"Total violations found: {df['violations'].sum()}")
print(f"\n{df[['rule', 'subreddit', 'priority', 'expected_confidence', 'violations', 'violation_rate']].to_string(index=False)}")

# Group by rule
print("\n" + "="*80)
print("SUMMARY BY RULE")
print("="*80)
for rule in df['rule'].unique():
    rule_df = df[df['rule'] == rule]
    print(f"\n{rule.upper().replace('_', ' ')}:")
    print(f"  Total violations: {rule_df['violations'].sum()}/{rule_df['total_comments'].sum()}")
    print(f"  Average violation rate: {rule_df['violation_rate'].mean():.2%}")
    print(f"  Best subreddit: {rule_df.loc[rule_df['violation_rate'].idxmax(), 'subreddit']} ({rule_df['violation_rate'].max():.2%})")

# Analyze hypothesis accuracy
print("\n" + "="*80)
print("HYPOTHESIS ACCURACY ANALYSIS")
print("="*80)

confidence_mapping = {
    'VERY_HIGH': 0.5,
    'HIGH': 0.3,
    'MODERATE_HIGH': 0.2,
    'MODERATE': 0.1,
    'LOW_MODERATE': 0.05,
    'LOW': 0.02
}

df['expected_rate'] = df['expected_confidence'].map(confidence_mapping)
df['hypothesis_correct'] = df['violation_rate'] >= df['expected_rate']

print(f"\nHypotheses validated: {df['hypothesis_correct'].sum()}/{len(df)} ({df['hypothesis_correct'].mean():.1%})")
print(f"\nBy priority:")
for priority in ['PRIMARY', 'HIGH', 'MEDIUM', 'LOW']:
    priority_df = df[df['priority'] == priority]
    if len(priority_df) > 0:
        correct = priority_df['hypothesis_correct'].sum()
        total = len(priority_df)
        print(f"  {priority}: {correct}/{total} ({correct/total:.1%})")

# Top performers
print("\n" + "="*80)
print("TOP 5 HIGHEST VIOLATION RATES")
print("="*80)
top5 = df.nlargest(5, 'violation_rate')[['rule', 'subreddit', 'priority', 'violation_rate']]
print(top5.to_string(index=False))

# Bottom performers
print("\n" + "="*80)
print("TOP 5 LOWEST VIOLATION RATES")
print("="*80)
bottom5 = df.nsmallest(5, 'violation_rate')[['rule', 'subreddit', 'priority', 'violation_rate']]
print(bottom5.to_string(index=False))

print(f"\n\nFull results saved to: wise_validation_summary.csv")
