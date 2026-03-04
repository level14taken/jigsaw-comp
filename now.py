class JigsawDataset(Dataset):
    def __init__(self, texts, labels,rule_ids, tokenizer, max_len, data_types=None):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_len = max_len
        self.rule_ids = rule_ids
        self.data_types = data_types if data_types is not None else [0] * len(texts)

    def __len__(self): return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        enc = self.tokenizer(
            text, padding='max_length', truncation=True, max_length=self.max_len, return_tensors="pt"
        )
        item = {k: v.squeeze(0) for k, v in enc.items()}
        item["labels"] = torch.tensor(self.labels[idx], dtype=torch.float)
        item['rule_ids']= torch.tensor(self.rule_ids[idx])
        item['data_types'] = torch.tensor(self.data_types[idx], dtype=torch.long)
        return item

class JigsawModel(nn.Module):
    def __init__(self, model_path):
        super().__init__()
        self.base = AutoModel.from_pretrained(model_path)
        self.drop = nn.Dropout(0.15)
        self.out = nn.Linear(self.base.config.hidden_size, 1)

    def forward(self, input_ids, attention_mask, data_types=None, labels=None, return_mixup_info=False):
        if self.training and data_types is not None and torch.rand(1) < 0.4:
            aug_indices = (data_types == 0).nonzero(as_tuple=True)[0]
            pseudo_indices = (data_types == 1).nonzero(as_tuple=True)[0]

            if len(aug_indices) > 0 and len(pseudo_indices) > 0:
                embeddings = self.base.embeddings(input_ids)

                min_len = min(len(aug_indices), len(pseudo_indices))
                if min_len > 0:
                    aug_subset = aug_indices[:min_len]
                    pseudo_subset = pseudo_indices[:min_len]

                    lam = np.random.beta(0.2, 0.2)

                    mixed_embeddings = embeddings.clone()
                    mixed_embeddings[aug_subset] = lam * embeddings[aug_subset] + (1 - lam) * embeddings[pseudo_subset]

                    outputs = self.base(inputs_embeds=mixed_embeddings, attention_mask=attention_mask)
                    pooled = outputs.last_hidden_state[:, 0]
                    logits = self.out(self.drop(pooled)).squeeze(1)

                    if return_mixup_info and labels is not None:
                        mixed_labels = labels.clone()
                        mixed_labels[aug_subset] = lam * labels[aug_subset] + (1 - lam) * labels[pseudo_subset]
                        return {'logits': logits, 'mixed_labels': mixed_labels, 'was_mixed': torch.tensor(True)}

                    return logits

        outputs = self.base(input_ids=input_ids, attention_mask=attention_mask)
        pooled = outputs.last_hidden_state[:, 0]
        logits = self.out(self.drop(pooled)).squeeze(1)

        if return_mixup_info:
            return {'logits': logits, 'mixed_labels': labels, 'was_mixed': torch.tensor(False)}

        return logits

