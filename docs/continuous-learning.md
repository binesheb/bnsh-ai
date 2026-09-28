# ARIV Continuous Learning Architecture

ARIV may continuously improve from newly available information and approved teacher models, but learning is separated into stages.

## Core principle

**Discovery does not equal training.**

Fresh information first enters a versioned knowledge layer. Model-weight changes require a candidate dataset, evaluation, and a promotion decision.

## Loop

```
Internet / approved sources
        ↓
Discovery
        ↓
Collection + provenance
        ↓
Policy / license / robots checks
        ↓
Extraction + normalization
        ↓
Deduplication + quality checks
        ↓
Knowledge Store
        │
        ├──→ Retrieval / RAG (fast knowledge updates)
        │
        └──→ Training Candidate Queue
                    ↓
             Teacher generation
                    ↓
             Filtering / verification
                    ↓
             Training experiment
                    ↓
             Evaluation suite
                    ↓
             Candidate checkpoint
                    ↓
             Promotion gate
                    ↓
                 ARIV vNext
```

## Learning modes

### 1. Retrieval learning

New information is indexed without changing model weights.

This should be the default mechanism for rapidly changing information.

### 2. Instruction adaptation

Approved teacher models can generate candidate examples. The examples are filtered, attributed, and evaluated before training.

### 3. Continued pretraining

Curated, licensed text/code/multimodal datasets can be used for continued pretraining when a measurable benefit is expected.

### 4. Distillation

Where technically and legally permitted, ARIV can learn from richer teacher signals such as logits.

## Autonomous operation

The system may automatically:

- discover candidate sources
- collect permitted content
- record provenance
- deduplicate data
- detect changes
- build candidate datasets
- run experiments
- execute evaluations
- compare checkpoints
- produce a release candidate

The system must **not silently replace the production ARIV model**.

Production promotion is a separate controlled stage.

## Trust boundaries

Every item should retain provenance including:

- source URL or source identifier
- retrieval timestamp
- content hash
- extraction method
- license/usage basis when known
- transformation history
- dataset/checkpoint that consumed it

## Evaluation gate

A candidate checkpoint should be compared with the current release for:

- multilingual quality
- factuality
- reasoning
- coding
- instruction following
- safety
- latency/resource usage
- regression tests
- contamination/leakage checks where applicable

A candidate that improves one benchmark but introduces unacceptable regressions must not be promoted automatically.

## Model lineage

Every checkpoint should have a machine-readable lineage:

```
ARIV-vNext
  ├── parent checkpoint
  ├── dataset versions
  ├── teacher models
  ├── training configuration
  ├── evaluation results
  └── software revision
```

This makes ARIV evolution reproducible and auditable.

## Security

The internet is an untrusted input.

The learning system must assume that web content can contain:

- malicious instructions
- poisoned training examples
- prompt injection
- duplicated/copy-pasted content
- fabricated claims
- malware or dangerous files
- unexpected personal information

Fetched content must be treated as **data, never as executable instructions**.

## Long-term goal

The goal is an AI system that can continuously acquire useful knowledge and improve through evidence-based training while retaining:

- model identity
- provenance
- reproducibility
- safety controls
- evaluation discipline
- human control over production releases
