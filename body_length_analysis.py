import pandas as pd
import numpy as np

# Read the CSV files
print("Reading files...")
train_df = pd.read_csv('train.csv')
reddit_df = pd.read_csv('reddit-removal-log.csv')

print(f"Train CSV shape: {train_df.shape}")
print(f"Reddit CSV shape: {reddit_df.shape}")
print()

# Calculate body lengths
print("Calculating body lengths...")
train_df['body_length'] = train_df['body'].fillna('').astype(str).str.len()
reddit_df['body_length'] = reddit_df['body'].fillna('').astype(str).str.len()

# Basic statistics
print("=" * 80)
print("BASIC LENGTH STATISTICS")
print("=" * 80)
print("\nTrain CSV Body Length Statistics:")
print(train_df['body_length'].describe())
print()
print("Reddit CSV Body Length Statistics:")
print(reddit_df['body_length'].describe())
print()

# Percentiles for more detailed comparison
percentiles = [0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99]
print("=" * 80)
print("PERCENTILE COMPARISON")
print("=" * 80)
print(f"{'Percentile':<12} {'Train CSV':<15} {'Reddit CSV':<15} {'Difference':<15}")
print("-" * 80)
for p in percentiles:
    train_val = train_df['body_length'].quantile(p)
    reddit_val = reddit_df['body_length'].quantile(p)
    diff = train_val - reddit_val
    print(f"{p*100:>6.0f}%      {train_val:>12.1f}    {reddit_val:>12.1f}    {diff:>12.1f}")
print()

# Length distribution bins
print("=" * 80)
print("LENGTH DISTRIBUTION (BINNED)")
print("=" * 80)
bins = [0, 50, 100, 200, 500, 1000, 2000, 5000, 10000, float('inf')]
labels = ['0-50', '50-100', '100-200', '200-500', '500-1K', '1K-2K', '2K-5K', '5K-10K', '10K+']

train_binned = pd.cut(train_df['body_length'], bins=bins, labels=labels)
reddit_binned = pd.cut(reddit_df['body_length'], bins=bins, labels=labels)

train_dist = train_binned.value_counts(normalize=True).sort_index() * 100
reddit_dist = reddit_binned.value_counts(normalize=True).sort_index() * 100

print(f"{'Length Range':<12} {'Train %':<12} {'Reddit %':<12} {'Diff %':<12}")
print("-" * 80)
for label in labels:
    train_pct = train_dist.get(label, 0)
    reddit_pct = reddit_dist.get(label, 0)
    diff = train_pct - reddit_pct
    print(f"{label:<12} {train_pct:>10.2f}%  {reddit_pct:>10.2f}%  {diff:>10.2f}%")
print()

# Statistical tests
from scipy import stats

print("=" * 80)
print("STATISTICAL ANALYSIS")
print("=" * 80)

# Kolmogorov-Smirnov test
ks_stat, ks_pvalue = stats.ks_2samp(train_df['body_length'], reddit_df['body_length'])
print(f"Kolmogorov-Smirnov Test:")
print(f"  KS Statistic: {ks_stat:.4f}")
print(f"  P-value: {ks_pvalue:.4e}")
print(f"  Interpretation: {'Distributions are DIFFERENT' if ks_pvalue < 0.05 else 'Distributions are SIMILAR'}")
print()

# Mann-Whitney U test (for medians)
u_stat, u_pvalue = stats.mannwhitneyu(train_df['body_length'], reddit_df['body_length'], alternative='two-sided')
print(f"Mann-Whitney U Test (comparing medians):")
print(f"  U Statistic: {u_stat:.4f}")
print(f"  P-value: {u_pvalue:.4e}")
print(f"  Interpretation: {'Medians are DIFFERENT' if u_pvalue < 0.05 else 'Medians are SIMILAR'}")
print()

# Check sampling bias by comparing ratio across length bins
print("=" * 80)
print("SAMPLING RATIO ANALYSIS")
print("=" * 80)
print("If train.csv was randomly sampled, the ratio should be constant across all length bins")
print()

train_counts = train_binned.value_counts().sort_index()
reddit_counts = reddit_binned.value_counts().sort_index()

overall_ratio = len(train_df) / len(reddit_df)
print(f"Overall sampling ratio: {overall_ratio:.4f} ({overall_ratio*100:.2f}%)")
print()
print(f"{'Length Range':<12} {'Train N':<12} {'Reddit N':<12} {'Ratio':<12} {'vs Overall':<15}")
print("-" * 80)
for label in labels:
    train_n = train_counts.get(label, 0)
    reddit_n = reddit_counts.get(label, 0)
    if reddit_n > 0:
        ratio = train_n / reddit_n
        ratio_diff = ((ratio / overall_ratio) - 1) * 100
        marker = "✓" if abs(ratio_diff) < 10 else "✗"
        print(f"{label:<12} {train_n:>10}   {reddit_n:>10}   {ratio:>10.4f}   {ratio_diff:>+8.1f}% {marker}")
    else:
        print(f"{label:<12} {train_n:>10}   {reddit_n:>10}   {'N/A':<10}   {'N/A':<12}")
print()
print("Legend: ✓ = within 10% of overall ratio (likely random), ✗ = deviates >10% (likely biased)")
print()

# Summary conclusion
print("=" * 80)
print("CONCLUSION")
print("=" * 80)
print("Based on the analysis above:")
print()
if ks_pvalue < 0.05:
    print("1. The distributions are statistically DIFFERENT (KS test p < 0.05)")
else:
    print("1. The distributions are statistically SIMILAR (KS test p >= 0.05)")

# Check if sampling ratios are consistent
ratio_diffs = []
for label in labels:
    train_n = train_counts.get(label, 0)
    reddit_n = reddit_counts.get(label, 0)
    if reddit_n > 0:
        ratio = train_n / reddit_n
        ratio_diff = abs((ratio / overall_ratio) - 1) * 100
        ratio_diffs.append(ratio_diff)

if ratio_diffs:
    avg_deviation = np.mean(ratio_diffs)
    if avg_deviation < 10:
        print("2. Sampling appears RANDOM across length bins (avg deviation < 10%)")
    else:
        print(f"2. Sampling appears BIASED across length bins (avg deviation = {avg_deviation:.1f}%)")
print()
print("If train.csv was randomly sampled from reddit-removal-log.csv across all lengths,")
print("we would expect:")
print("  - Similar distribution shapes")
print("  - Consistent sampling ratios across all length bins")
print("  - No systematic over/under-representation of any length range")
