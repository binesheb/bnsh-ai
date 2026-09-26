# BNSH Model Specification

This document records requirements for future BNSH model releases.

## Public goals

A BNSH model should be:

- downloadable
- locally runnable
- documented
- versioned
- evaluated
- usable through standard developer interfaces

## Multilingual focus

Indian languages are a core research direction. Exact language coverage and quality targets will be established through benchmark results rather than marketing claims.

Initial research languages may include English, Malayalam, Hindi, Tamil, Kannada, and Telugu.

## Release requirements

Before a public model release, document:

- architecture
- parameter count
- tokenizer
- training compute
- training data sources and licenses where legally possible
- fine-tuning data
- evaluation methodology
- known limitations
- safety considerations
- supported inference formats
- license

## Important distinction

The repository's MIT license applies to the source code unless a future component states otherwise. Model weights, datasets, and upstream components may have separate licenses and must be reviewed individually before distribution.
