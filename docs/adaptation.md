# Learning from Existing Models

ARIV is designed to improve using existing models without becoming a wrapper or rebrand of those models.

## Adaptation layers

### Teacher data

This is the broadest compatibility mechanism. A teacher such as an open-weight model or an authorized model API can answer a carefully designed task set. After filtering and evaluation, those examples can become ARIV instruction-tuning data.

### Distillation

Where technically and legally permitted, a compatible teacher can provide richer signals such as logits. This can improve sample efficiency but requires compatible access and substantially more infrastructure.

### Retrieval and tools

An existing model can also act as a temporary knowledge or tool layer during development. Retrieved information should not automatically become model training data; provenance and usage rights must be established first.

## What ARIV should not do

ARIV should not:

- copy another model's weights and call them ARIV weights
- automatically ingest arbitrary model outputs
- bypass model or dataset licenses
- treat every generated answer as ground truth
- claim capabilities without evaluation

## Goal

Build a model that can **learn from the broader open-model ecosystem while maintaining its own identity, weights, evaluation, provenance, and release history**.
