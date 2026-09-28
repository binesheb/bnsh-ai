# BNSH Model Specification

## Identity

**BNSH is a model family.**

The name BNSH must not be used to imply that an external model is an official BNSH checkpoint.

The repository contains both:

1. **BNSH models** — models trained/released as part of the BNSH model family.
2. **BNSH ecosystem software** — runtime, training, evaluation, model management, SDKs, APIs, and deployment tooling.

## Public goals

A BNSH model should be:

- downloadable
- locally runnable
- documented
- versioned
- evaluated
- usable through standard developer interfaces
- suitable for research and product integration according to its release license

## Model variants

The family may contain:

- BNSH — general foundation model
- BNSH-Instruct — instruction-following model
- BNSH-Reason — reasoning model
- BNSH-Coder — coding model
- BNSH-Vision — vision-language model

These names describe intended capabilities, not guarantees. A release should only claim capabilities supported by evaluation.

## Multilingual focus

Indian languages are a core research direction. Initial research may include English, Malayalam, Hindi, Tamil, Kannada, and Telugu.

Language quality must be demonstrated through documented evaluations rather than branding claims.

## Release requirements

Before a public BNSH model release, document:

- architecture
- parameter count
- tokenizer
- context length
- training compute
- training data sources and licenses where legally possible
- fine-tuning data
- evaluation methodology
- known limitations
- safety considerations
- supported inference formats
- model license
- revision/checksum information

## External models

The BNSH ecosystem may support external open models through adapters and inference backends.

External models must retain their original identity and applicable license. They must not be represented as BNSH checkpoints.

## Code versus model licensing

The repository's software license does not automatically determine the license of future model weights or datasets. Every model release must publish its own applicable licensing information.
