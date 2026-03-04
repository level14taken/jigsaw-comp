if os.getenv('KAGGLE_IS_COMPETITION_RERUN'):
    # Load and prepare test data for training
    df_test = pd.read_csv(test_path)
    df_test["text"] = df_test["rule"] + " [SEP] " + df_test["body"]

    print("\n===== Single Fold Training: Test data for training, Train data for validation =====")

    # Use test data for training, all train data for validation
    train_ds = JigsawDataset(df_test['text'].tolist(), df_test['label'].tolist(), tokenizer, MAX_LEN, df=df, df_test=df_test)
    val_ds = JigsawDataset(df['text'].tolist(), df['label'].tolist(), tokenizer, MAX_LEN)
    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=BATCH_SIZE)
    
        # Initialize classification model and load MLM pre-trained weights
        model = JigsawModel(MODEL_PATH).to(DEVICE)
         # Load MLM pre-trained base model weights
        mlm_state = torch.load("pretrained.bin", map_location=DEVICE)
        mlm_state= {k.replace('module.',''):v for k,v in mlm_state.items()}    
        model.load_state_dict(mlm_state)
        
        for name, param in model.named_parameters():
            if name.startswith('base.') and any(f'layer.{i}' in name for i in range(7)) :#what was left untrained then is left untrained here.
                param.requires_grad = False
                
        optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
    
    best_loss = 10
    for epoch in range(EPOCHS):
        print(f"Epoch {epoch+1}/{EPOCHS}")
        loss = train_one_epoch(model, train_loader, optimizer, None)
        val_auc, val_loss, val_preds = validate(model, val_loader)

        print(f"Loss: {loss:.4f}, Val Loss: {val_loss:.4f}, Val AUC: {val_auc:.4f}")
        if val_loss < best_loss:
            best_loss = val_loss
            torch.save(model.state_dict(), "model_best.bin")

    print(f"Training completed. Best validation loss: {best_loss:.4f}")


# all_truths=[]
# all_rules=[]
# folds = StratifiedKFold(n_splits=NFOLDS, shuffle=True, random_state=SEED)
# for fold, (tr_idx, val_idx) in enumerate(folds.split(df, df["label"])):
#     all_truths.append(df.iloc[val_idx].label)
#     all_rules.append(df.iloc[val_idx].rule)

# preddf= pd.DataFrame(columns=['preds','truths','rule'])
# preddf.preds=pd.concat(all_preds,ignore_index=True)
# preddf.rule= pd.concat(all_rules,ignore_index=True)
# preddf.truths= pd.concat(all_truths,ignore_index=True)

# print(preddf.groupby('rule').apply(lambda group: roc_auc_score(group['truths'],group['preds'])))

if os.getenv('KAGGLE_IS_COMPETITION_RERUN'):
    sample = pd.read_csv(sample_sub_path)
    df_test_inference = pd.read_csv(test_path)
    df_test_inference["text"] = df_test_inference["rule"] + " [SEP] " + df_test_inference["body"]

    # Load single trained model
    model = JigsawModel(MODEL_PATH).to(DEVICE)
    wts = torch.load("model_best.bin", map_location=DEVICE)
    wts = {k.replace('module.',''):v for k,v in wts.items()}

    model.load_state_dict(wts)
    model.eval()

    test_ds = JigsawDataset(df_test_inference['text'].tolist(), [0]*len(df_test_inference), tokenizer, MAX_LEN)
    test_loader = DataLoader(test_ds, batch_size=BATCH_SIZE)

    test_preds = []
    with torch.no_grad():
        for batch in test_loader:
            ids = batch['input_ids'].to(DEVICE)
            mask = batch['attention_mask'].to(DEVICE)
            logits = model(ids, mask)
            test_preds.extend(torch.sigmoid(logits).cpu().numpy())


if os.getenv('KAGGLE_IS_COMPETITION_RERUN'):
    sample["rule_violation"] = test_preds
    sample.to_csv("submission.csv", index=False)
    print("✅ Submission saved as submission.csv")
else:
    !touch submission.csv
    
!head -n 4 submission.csv
