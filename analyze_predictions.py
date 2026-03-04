import pandas as pd
import numpy as np

print("Loading deberta predictions...")
deberta_df = pd.read_csv('pseudo_labeled_data_with_predictions.csv')
print(f"Deberta shape: {deberta_df.shape}")
print(f"Deberta columns: {list(deberta_df.columns)}")
print()

print("Loading LLM predictions...")
llm1 = pd.read_csv('LLMensemble/test1.csv')
llm2 = pd.read_csv('LLMensemble/test2.csv')
llm3 = pd.read_csv('LLMensemble/test3.csv')

print(f"LLM1 shape: {llm1.shape}")
print(f"LLM1 columns: {list(llm1.columns)}")
print()
print(f"LLM2 shape: {llm2.shape}")
print(f"LLM2 columns: {list(llm2.columns)}")
print()
print(f"LLM3 shape: {llm3.shape}")
print(f"LLM3 columns: {list(llm3.columns)}")
print()

print("="*80)
print("DEBERTA PREDICTIONS ANALYSIS")
print("="*80)
print("\nFirst few rows:")
print(deberta_df.head())
print("\nPrediction statistics:")
print(deberta_df['mean_prediction'].describe())
print("\nRule distribution:")
print(deberta_df['rule'].value_counts())
print()

print("="*80)
print("LLM PREDICTIONS ANALYSIS")
print("="*80)

for i, llm_df in enumerate([llm1, llm2, llm3], 1):
    print(f"\n--- LLM{i} ---")
    print(f"First few rows:")
    print(llm_df.head(2))

    if 'qwen' in llm_df.columns:
        print(f"\nQwen predictions stats:")
        print(llm_df['qwen'].describe())

    if 'llama' in llm_df.columns:
        print(f"\nLlama predictions stats:")
        print(llm_df['llama'].describe())

    if 'rule_violation' in llm_df.columns:
        print(f"\nRule violation stats:")
        print(llm_df['rule_violation'].describe())

print("\n" + "="*80)
print("CHECKING DATA OVERLAP")
print("="*80)

if 'body' in deberta_df.columns and 'body' in llm1.columns:
    print("\nChecking if bodies match between datasets...")
    print(f"Unique bodies in deberta: {deberta_df['body'].nunique()}")
    print(f"Unique bodies in llm1: {llm1['body'].nunique()}")
    print(f"Unique bodies in llm2: {llm2['body'].nunique()}")
    print(f"Unique bodies in llm3: {llm3['body'].nunique()}")

    common_bodies = set(deberta_df['body']) & set(llm1['body'])
    print(f"\nCommon bodies between deberta and llm1: {len(common_bodies)}")

print("\n" + "="*80)
print("INTERACTIVE ANALYSIS")
print("="*80)
print("\nAvailable dataframes:")
print("- deberta_df: Deberta predictions")
print("- llm1, llm2, llm3: LLM predictions")
print("\nYou can now use these in an interactive session!")
