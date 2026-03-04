def get_subreddit_proportions():
    """Get subreddit proportions for each rule from test data"""
    prop_df = pd.concat((pd.read_csv(test_path),pd.read_csv(train_path)))
    
    proportions = {}
    for rule in prop_df["rule"].unique():
        rule_data = prop_df[prop_df["rule"] == rule]
        subreddit_counts = rule_data["subreddit"].value_counts()
        subreddit_props = subreddit_counts / subreddit_counts.sum()
        proportions[rule] = subreddit_props.to_dict()
    
    return proportions, len(prop_df)
    
def sample_unlabelled_data(multiplier=5):
    """Sample unlabelled data maintaining test data proportions"""
    proportions, test_size = get_subreddit_proportions()
    
    total_sample_size = test_size * multiplier
    sampled_data = []
    
    # Calculate samples per rule based on test data rule distribution
    rule_counts = augmented_df["rule"].value_counts()
    rule_proportions = rule_counts / rule_counts.sum()

    # unlabelled_df= pd.read_csv(unlabelled_path)
    excluded_values = augmented_df['body'].values# + train_df[['body', 'positive_example_1', 'positive_example_2', 'negative_example_1', 'negative_example_2']].values.ravel()
    global unlabelled_df
    unlabelled_df = unlabelled_df.query('body not in @excluded_values')
    
    unlabelled_df.drop(unlabelled_df[(unlabelled_df['body'].str.len() > 2000)].index, inplace=True)    #filter out body present in test,examples
    # print(unlabelled_df.shape)
    unlabelled_df['body_lower']=unlabelled_df.body.str.lower()
    unlabelled_df.drop_duplicates(subset=['body_lower'],keep='first',inplace=True,ignore_index=True)
    unlabelled_df.drop(columns=['body_lower'],inplace=True)
    # print(unlabelled_df.shape,'Only Unique')
    
    import tqdm
    for rule, rule_prop in tqdm.tqdm(rule_proportions.items()):
        rule_sample_size = int(total_sample_size * rule_prop)
        subreddit_props = proportions[rule]
        
        rule_samples = []
        for subreddit, sub_prop in subreddit_props.items():
            subreddit_sample_size = int(rule_sample_size * sub_prop)
            
            # Sample from unlabelled data for this subreddit
            subreddit_data = unlabelled_df[unlabelled_df["subreddit"].str.lower().str.strip() == subreddit.lower().strip()]
            if len(subreddit_data) ==0 or subreddit_sample_size==0: 
                # Fallback: sample from any data for this rule
                continue
                # subreddit_data = unlabelled_df[unlabelled_df["rule"] == rule]

            if len(subreddit_data) >= subreddit_sample_size:
                sampled = subreddit_data.sample(n=subreddit_sample_size, random_state=42)
            else:
                # If not enough data, sample with replacement
                sampled = subreddit_data.copy()
            
            sampled = sampled.copy()
            sampled["rule"] = rule
            rule_samples.append(sampled)
        
        if rule_samples:
            sampled_data.append(pd.concat(rule_samples, axis=0))
    
    # Combine all samples and shuffle
    final_sample = pd.concat(sampled_data, axis=0).reset_index(drop=True)
    final_sample = final_sample.sample(frac=1, random_state=42).reset_index(drop=True)
    
    return final_sample