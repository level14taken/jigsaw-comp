# Jigsaw Agile Community Rules

Kaggle competition entry: classify Reddit comments as violating one of 6 community rules, using a data mining pipeline to surface training signal and a deep mutual learning ensemble for final predictions.

## Problem

Binary classification — does a comment violate a given rule?

| Rule | Description |
|------|-------------|
| `financial_advice` | Personal investment, tax, or career recommendations |
| `medical_advice` | Medical diagnoses or treatment recommendations |
| `illegal_activity` | Promoting drugs, violence, exploitation, or crime |
| `spoilers` | Revealing plot details that ruin entertainment |
| `advertising` | Spam, referral links, or promotional content |
| `legal_advice` | Offering or requesting legal advice |

## Approach

### Phase 1 — Data Mining

The official training data was sparse. To build a richer training set, the Reddit Removal Log (2M moderated comments) was sampled across 100+ subreddits over 9 rounds to identify high-signal subreddit–rule pairs.

**Top sources by violation rate:**

| Subreddit | Rule | Violation Rate |
|-----------|------|---------------|
| anime | spoilers | 18% |
| videos | advertising | 16% |
| asoiaf | spoilers | 14% |
| personalfinance | financial_advice | 13% |
| incels | illegal_activity | 12% |
| suicidewatch | illegal_activity | 10% |

69 combinations tested · 5.2% overall violation rate · ~2,700 violations collected from top sources

### Phase 2 — Modeling

**Baseline — DeBERTa v3-base** (`notebooks/01_deberta_baseline.ipynb`)
- BCEWithLogitsLoss, data augmentation from competition positive/negative examples
- ~0.89 AUC on validation

**Final — Deep Mutual Learning Ensemble** (`notebooks/06_deep_mutual_learning_ensemble.ipynb`)
- Three models fine-tuned simultaneously with mutual KL-divergence distillation:
  - Model A: Qwen2.5-14B + LoRA (50% weight)
  - Model B: Qwen2.5-8B + LoRA (30% weight)
  - Model C: Qwen3-Guard-4B + LoRA (20% weight)
- 4-bit quantization · pseudo-labeling on 100K unlabeled comments · multi-GPU inference

## Project Structure

```
notebooks/    7 key notebooks from baseline to final submission
scripts/      Training, inference, sampling, and analysis scripts
data/
  raw/        Competition files (train.csv, test.csv)
  sampling/   ~100 CSVs across 9 subreddit sampling rounds
  analysis/   Round results, summaries, and prediction CSVs
  submissions/ Kaggle submission files
docs/         Methodology write-ups and round-by-round summaries
papers/       3 referenced research papers
```

## Usage

```bash
# Train DeBERTa baseline
python scripts/train.py

# Run multi-GPU inference
python scripts/inference.py

# Sample comments from Reddit Removal Log
python scripts/sampling.py
```

## Key Notebooks

| Notebook | Description |
|----------|-------------|
| `01_deberta_baseline` | DeBERTa v3-base classifier — competition baseline |
| `02_qwen14b_inference` | Qwen2.5-14B zero-shot inference |
| `03_llm_deberta_hybrid` | Hybrid LLM scoring + DeBERTa classifier |
| `04_ensemble` | Prediction blending strategies |
| `05_pseudo_labeling` | Pseudo-label generation from unlabeled data |
| `06_deep_mutual_learning_ensemble` | Final submission — 3-model mutual distillation |
| `07_qwen3_embedding` | Qwen3 embedding + semantic similarity approach |

## References

- Chandrasekharan et al. (2018) — *You Can't Stay Here: The Efficacy of Reddit's 2015 Ban*
- arXiv:[2309.14517](https://arxiv.org/abs/2309.14517)
- arXiv:[2505.09388](https://arxiv.org/abs/2505.09388)
