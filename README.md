# BNSH AI

**Open Indian-built multilingual AI.**

BNSH AI is an open model and AI runtime project focused on multilingual intelligence, local inference, developer access, and edge deployment.

The long-term goal is to build a family of openly available foundation models that anyone can download, run, integrate, fine-tune, and build products with, subject to the project's license.

## Project vision

BNSH AI is designed as an independent intelligence layer that can run:

- locally on personal computers and workstations
- on cloud GPU infrastructure
- on private enterprise servers
- on edge devices through compact/quantized models
- as the AI core of [BINESH OS](https://github.com/binesheb/binesh-os)

BNSH AI is not intended to be only a hosted chatbot. Model weights, tooling, evaluation, runtime interfaces, and documentation are first-class parts of the project.

## Planned model family

| Model | Purpose | Status |
|---|---|---|
| BNSH-Base | Base language model | Planned |
| BNSH-Instruct | Instruction-following/chat | Planned |
| BNSH-Reason | Reasoning | Planned |
| BNSH-Coder | Code generation | Planned |
| BNSH-Vision | Vision-language | Planned |

Model names are provisional until the corresponding releases are established.

## Architecture

```
Applications
    |
BNSH SDK / REST API
    |
BNSH Runtime
    |
Model + Tokenizer + Inference Engine
    |
Local / Cloud / Edge Hardware
```

BINESH OS can consume the same runtime through a stable AI interface, allowing the operating system to use local or remote BNSH models without coupling OS services to one specific model size.

## Repository layout

```
bnsh-ai/
├── bnsh/          # Python runtime and public APIs
├── training/      # Training and fine-tuning pipeline
├── datasets/      # Dataset specifications and tooling
├── evaluation/    # Benchmarks and evaluation harness
├── configs/       # Reproducible configuration
├── examples/      # Developer examples
├── scripts/       # Developer/CI utilities
├── tests/         # Automated tests
└── docs/          # Architecture, roadmap and model specifications
```

## Current status

**Pre-alpha — architecture and tooling phase.**

The first milestone is to establish a reproducible runtime, dataset/evaluation pipeline, and small-model development workflow before attempting larger-scale pretraining.

## Principles

1. Open by design.
2. Reproducible where practical.
3. Multilingual from the beginning.
4. Local inference is a first-class capability.
5. Model and runtime are separate components.
6. Evaluation must accompany model releases.
7. BINESH OS integration must use stable interfaces rather than model-specific coupling.
8. Training data and upstream licenses must be documented before distribution.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Security

See [SECURITY.md](SECURITY.md).

## License

See [LICENSE](LICENSE).

## Local model experimentation

The core package is intentionally lightweight. For local open-weight model experimentation, install the optional Transformers backend:

```bash
pip install -e ".[transformers]"
```

Then use `TransformersBackend` with `BNSHRuntime`. See [docs/transformers.md](docs/transformers.md).

The first backend is an interoperability layer; it is not yet the BNSH foundation model itself. The project will establish its own training and evaluation pipeline before publishing BNSH model checkpoints.
