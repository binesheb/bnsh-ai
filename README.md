# BNSH AI

**Open Indian-built multilingual AI.**

BNSH AI is an open model and AI runtime project focused on multilingual intelligence, local inference, developer access, and edge deployment.

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

The bootstrap creates an isolated environment, installs BNSH AI, and runs the validation suite. See [docs/bootstrap.md](docs/bootstrap.md).

## Project vision

BNSH AI is designed to become an openly available family of foundation models that people can download, run, integrate, fine-tune, and build products with, subject to each release's license.

It can run locally on personal computers, workstations, private servers, cloud infrastructure, and edge systems. BNSH AI is also intended to provide the intelligence layer for [BINESH OS](https://github.com/binesheb/binesh-os).

## Planned model family

| Model | Purpose | Status |
|---|---|---|
| BNSH-Base | Base language model | Planned |
| BNSH-Instruct | Instruction-following/chat | Planned |
| BNSH-Reason | Reasoning | Planned |
| BNSH-Coder | Code generation | Planned |
| BNSH-Vision | Vision-language | Planned |

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

## Current status

**Pre-alpha — runtime and model-development foundation.**

The repository currently contains the runtime abstraction, backend interface, optional Transformers integration, tests, CI, and bootstrap tooling. The first BNSH foundation model has not yet been released.

## Principles

1. Open by design.
2. Reproducible where practical.
3. Multilingual from the beginning.
4. Local inference is first-class.
5. Model and runtime are separate.
6. Evaluation accompanies model releases.
7. BINESH OS uses stable AI interfaces.
8. Training data and upstream licenses must be documented.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Security

See [SECURITY.md](SECURITY.md).

## License

See [LICENSE](LICENSE).
