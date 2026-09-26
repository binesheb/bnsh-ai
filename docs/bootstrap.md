# BNSH Bootstrap

BNSH AI is designed to be deployable from a clean machine with a small number of prerequisites.

## Linux / macOS

From a shell:

```bash
curl -fsSL https://raw.githubusercontent.com/binesheb/bnsh-ai/main/bootstrap.sh | bash
```

Or clone first:

```bash
git clone https://github.com/binesheb/bnsh-ai.git
cd bnsh-ai
./bootstrap.sh
```

The script checks Git and Python 3.10+, creates an isolated virtual environment, installs the project and development dependencies, and runs the test suite.

## Windows

Run the PowerShell bootstrap script from a checkout:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\bootstrap.ps1
```

## Local model installation

The default bootstrap intentionally does **not** install PyTorch or large model dependencies. This keeps the base deployment fast and portable.

After bootstrap, install optional local inference support:

```bash
pip install -e ".[transformers]"
```

Future releases will provide hardware-specific bootstrap profiles such as CPU, NVIDIA CUDA, AMD/ROCm where supported, and edge deployments.

## Bootstrap design rules

- Idempotent: rerunning should reuse the checkout and virtual environment.
- No credentials required.
- No model weights are silently downloaded by the base installer.
- Installation must be reproducible.
- Hardware-specific dependencies remain opt-in.
- Bootstrap must validate the installation before declaring success.
