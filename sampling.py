import pandas as pd
from constants import DATA_PATH


def get_test_subreddit_proportions():
    """Get subreddit proportions for each rule from test data"""
    test_df = pd.read_csv(f"{DATA_PATH}/test.csv")
    
    proportions = {}
    for rule in test_df["rule"].unique():
        rule_data = test_df[test_df["rule"] == rule]
        subreddit_counts = rule_data["subreddit"].value_counts()
        subreddit_props = subreddit_counts / subreddit_counts.sum()
        proportions[rule] = subreddit_props.to_dict()
    
    return proportions, len(test_df)


def sample_unlabelled_data(unlabelled_path, total_test_size, multiplier=5):
    """Sample unlabelled data maintaining test data proportions"""
    unlabelled_df = pd.read_csv(unlabelled_path)
    proportions, test_size = get_test_subreddit_proportions()
    
    total_sample_size = total_test_size * multiplier
    sampled_data = []
    
    # Calculate samples per rule based on test data rule distribution
    test_df = pd.read_csv(f"{DATA_PATH}/test.csv")
    rule_counts = test_df["rule"].value_counts()
    rule_proportions = rule_counts / rule_counts.sum()
    
    for rule, rule_prop in rule_proportions.items():
        rule_sample_size = int(total_sample_size * rule_prop)
        subreddit_props = proportions[rule]
        
        rule_samples = []
        for subreddit, sub_prop in subreddit_props.items():
            subreddit_sample_size = int(rule_sample_size * sub_prop)
            
            # Sample from unlabelled data for this subreddit
            subreddit_data = unlabelled_df[unlabelled_df["subreddit"] == subreddit]
            
            if len(subreddit_data) >= subreddit_sample_size:
                sampled = subreddit_data.sample(n=subreddit_sample_size, random_state=42)
            else:
                # If not enough data, sample with replacement
                sampled = subreddit_data.sample(n=subreddit_sample_size, replace=True, random_state=42)
            
            sampled = sampled.copy()
            sampled["rule"] = rule
            rule_samples.append(sampled)
        
        if rule_samples:
            sampled_data.append(pd.concat(rule_samples, axis=0))
    
    # Combine all samples and shuffle
    final_sample = pd.concat(sampled_data, axis=0).reset_index(drop=True)
    final_sample = final_sample.sample(frac=1, random_state=42).reset_index(drop=True)
    
    return final_sample