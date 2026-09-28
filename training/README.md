# ARIV Training Pipeline

This directory contains reproducible building blocks for training ARIV models.

The initial objective is a **small-scale end-to-end experiment** that validates:

1. dataset ingestion
2. dataset validation
3. tokenizer integration
4. causal language-model training
5. checkpoint saving
6. evaluation
7. model metadata generation

The first experiment is not intended to produce a competitive foundation model. It validates the pipeline before larger compute is committed.

## Pipeline

```
Raw data
  ↓
Dataset manifest
  ↓
Validation / filtering
  ↓
Tokenizer
  ↓
Tokenized dataset
  ↓
Training
  ↓
Checkpoint
  ↓
Evaluation
  ↓
ARIV release candidate
```

## Data rule

Only data with documented provenance and a permitted usage basis should enter a release training set. Do not commit large datasets, model weights, secrets, or scraped data to this repository.

See `data/README.md` and `docs/data-governance.md`.
