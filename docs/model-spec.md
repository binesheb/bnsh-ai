# ARIV Model Specification

## Identity

**ARIV is the foundation-model family created by BNSH AI.**

The naming hierarchy is:

- **BNSH AI** — the overall open AI ecosystem.
- **ARIV** — the foundation-model family.
- **BNSH Runtime** — the runtime and integration layer.
- **BNSH SDK/API** — developer interfaces.
- **BINESH OS** — an important operating-system and edge deployment target.

The name ARIV must not be used to imply that an external model is an official ARIV checkpoint.

## Model variants

The family may contain:

- **ARIV** — general foundation model
- **ARIV-Instruct** — instruction following and chat
- **ARIV-Reason** — reasoning
- **ARIV-Coder** — code generation
- **ARIV-Vision** — vision-language

Size variants may use names such as ARIV-1B, ARIV-3B, ARIV-7B, or larger variants when supported by actual releases.

These names describe intended capabilities, not guarantees. A release should only claim capabilities supported by documented evaluation.

## Multilingual focus

Indian languages are a core research direction. Initial research may include English, Malayalam, Hindi, Tamil, Kannada, and Telugu.

Language quality must be demonstrated through documented evaluations rather than branding claims.

## Public goals

An ARIV release should be:

- downloadable
- locally runnable
- documented
- versioned
- evaluated
- usable through standard developer interfaces
- suitable for research and product integration according to its release license

## Release requirements

Before a public ARIV model release, document:

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

External models retain their original identity and applicable license. They must not be represented as ARIV checkpoints.

## Code versus model licensing

The BNSH software license does not automatically determine the license of future ARIV model weights or datasets. Every model release must publish its own applicable licensing information.
