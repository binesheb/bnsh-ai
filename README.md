# BNSH AI

**Open Indian-built multilingual AI.**

BNSH AI is the open AI ecosystem. **ARIV is its foundation-model family**, designed for multilingual intelligence, local inference, developer access, and deployment across personal computers, servers, cloud infrastructure, and BINESH OS.

> **BNSH AI is the ecosystem. ARIV is the model family. BNSH Runtime is the infrastructure around ARIV and other supported models.**

## ARIV model family

The project is intended to produce its own ARIV model checkpoints rather than being only a wrapper around another model family.

Planned releases include:

| Model | Purpose | Status |
|---|---|---|
| **ARIV** | General-purpose foundation model | Planned |
| **ARIV-Instruct** | Instruction following and chat | Planned |
| **ARIV-Reason** | Reasoning | Planned |
| **ARIV-Coder** | Code generation | Planned |
| **ARIV-Vision** | Vision-language | Planned |

Size variants may eventually include models such as ARIV-1B, ARIV-3B, ARIV-7B and larger architectures. Exact sizes will be determined by training results and available compute.

Existing open models may be supported as development/inference backends, but they are **not BNSH models**.

## One-command bootstrap

Linux/macOS:

```bash
curl -fsSL https://raw.githubusercontent.com/binesheb/bnsh-ai/main/bootstrap.sh | bash
```

Windows PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\bootstrap.ps1
```

## Architecture

```
                    BNSH AI
                       │
             ┌─────────┴─────────┐
             │                   │
        BNSH Models        BNSH Ecosystem
             │                   │
   ┌─────────┼─────────┐   ┌─────┼──────────┐
   │         │         │   │     │          │
 Base    Instruct   Reason Runtime Training Evaluation
   │         │         │   │     │          │
   └─────────┴─────────┘   └─────┼──────────┘
                                 │
                           BNSH SDK / API
                                 │
                 ┌───────────────┼───────────────┐
                 │               │               │
              Windows          Linux          BINESH OS
```

BINESH OS is an important consumer and deployment target, but BNSH models remain independent and usable by anyone.

## Runtime

The runtime provides a stable interface between applications and models:

```python
from bnsh import BNSHRuntime

ai = BNSHRuntime(model="BNSH")

# configured inference backend
response = ai.chat("Hello")
```

The CLI is part of the BNSH ecosystem:

```bash
bnsh model list
bnsh model info BNSH
bnsh chat --model BNSH "Hello"
```

## Learning from existing models

ARIV is designed to learn from compatible existing models through explicit adaptation workflows.

Supported research paths include:

- teacher-generated instruction data
- knowledge distillation where technically and legally permitted
- parameter-efficient adaptation
- retrieval/tool-assisted data generation
- evaluation and filtering before training

External models remain external models. Their outputs, weights, licenses, and provenance are tracked separately from ARIV.

See [docs/adaptation.md](docs/adaptation.md).

## Model lifecycle

```
Research
   ↓
Data governance
   ↓
Dataset preparation
   ↓
Tokenizer
   ↓
Pretraining
   ↓
BNSH checkpoint
   ↓
Instruction tuning
   ↓
Evaluation
   ↓
Model release
   ↓
Download / local inference / API / fine-tuning
```

## Current status

**Pre-alpha — runtime and model-development foundation.**

The repository currently contains the runtime abstraction, backend interface, optional Transformers integration, model registry, tests, CI, bootstrap tooling, dataset schema, and the first reproducible ARIV training experiment foundation.

**No official BNSH foundation-model checkpoint has been released yet.**

## Principles

1. BNSH models are first-class open models.
2. Open by design.
3. Reproducible where practical.
4. Multilingual from the beginning.
5. Local inference is first-class.
6. Model and runtime are separate.
7. Evaluation accompanies model releases.
8. BINESH OS uses stable AI interfaces.
9. Training data and upstream licenses must be documented.
10. External models can be supported without being rebranded as BNSH.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Security

See [SECURITY.md](SECURITY.md).

## License

See [LICENSE](LICENSE).
