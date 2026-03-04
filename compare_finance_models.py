import pandas as pd
import numpy as np

print("Loading CSV files...")
df_14b = pd.read_csv('predictions_unlabelled_finance_14b.csv')
df_32b = pd.read_csv('predictions_unlabelled_finance_32b.csv')

print(f"\n{'='*60}")
print("BASIC INFO")
print(f"{'='*60}")
print(f"14b shape: {df_14b.shape}")
print(f"32b shape: {df_32b.shape}")
print(f"\n14b columns: {list(df_14b.columns)}")
print(f"32b columns: {list(df_32b.columns)}")

print(f"\n{'='*60}")
print("FIRST FEW ROWS")
print(f"{'='*60}")
print("\n14b first 5 rows:")
print(df_14b.head())
print("\n32b first 5 rows:")
print(df_32b.head())

print(f"\n{'='*60}")
print("STATISTICAL SUMMARY")
print(f"{'='*60}")
print("\n14b describe:")
print(df_14b.describe())
print("\n32b describe:")
print(df_32b.describe())

print(f"\n{'='*60}")
print("VALUE DISTRIBUTIONS")
print(f"{'='*60}")
for col in df_14b.columns:
    if col in df_32b.columns:
        print(f"\n{col} - 14b value counts:")
        print(df_14b[col].value_counts().head(20))
        print(f"\n{col} - 32b value counts:")
        print(df_32b[col].value_counts().head(20))

print(f"\n{'='*60}")
print("MISSING VALUES")
print(f"{'='*60}")
print("\n14b missing values:")
print(df_14b.isnull().sum())
print("\n32b missing values:")
print(df_32b.isnull().sum())

print(f"\n{'='*60}")
print("UNIQUE VALUES")
print(f"{'='*60}")
print("\n14b unique counts:")
print(df_14b.nunique())
print("\n32b unique counts:")
print(df_32b.nunique())

print(f"\n{'='*60}")
print("CHECKING FOR WEIRD PATTERNS IN 14B")
print(f"{'='*60}")

prediction_cols = [col for col in df_14b.columns if 'prediction' in col.lower() or col not in ['id', 'ID']]
for col in prediction_cols:
    if col in df_14b.columns:
        print(f"\n{col} analysis:")
        print(f"  14b - min: {df_14b[col].min()}, max: {df_14b[col].max()}, mean: {df_14b[col].mean():.4f}, std: {df_14b[col].std():.4f}")
        if col in df_32b.columns:
            print(f"  32b - min: {df_32b[col].min()}, max: {df_32b[col].max()}, mean: {df_32b[col].mean():.4f}, std: {df_32b[col].std():.4f}")

        print(f"  14b - zeros: {(df_14b[col] == 0).sum()}, ones: {(df_14b[col] == 1).sum()}")
        if col in df_32b.columns:
            print(f"  32b - zeros: {(df_32b[col] == 0).sum()}, ones: {(df_32b[col] == 1).sum()}")

        if col in df_32b.columns:
            diff = np.abs(df_14b[col] - df_32b[col])
            print(f"  Absolute difference - mean: {diff.mean():.4f}, max: {diff.max():.4f}, median: {diff.median():.4f}")
            print(f"  Correlation: {df_14b[col].corr(df_32b[col]):.4f}")

print(f"\n{'='*60}")
print("ROWS WITH LARGEST DIFFERENCES")
print(f"{'='*60}")
if prediction_cols and prediction_cols[0] in df_32b.columns:
    col = prediction_cols[0]
    diff = np.abs(df_14b[col] - df_32b[col])
    top_diff_idx = diff.nlargest(10).index

    comparison = pd.DataFrame({
        'index': top_diff_idx,
        '14b': df_14b.loc[top_diff_idx, col].values,
        '32b': df_32b.loc[top_diff_idx, col].values,
        'diff': diff.loc[top_diff_idx].values
    })
    print(f"\nTop 10 rows with largest differences in {col}:")
    print(comparison)

print("\nAnalysis complete!")
