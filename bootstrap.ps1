$ErrorActionPreference = "Stop"

# BNSH AI bootstrap installer for Windows PowerShell.
# Usage:
#   powershell -ExecutionPolicy Bypass -File .\bootstrap.ps1

$RepoUrl = if ($env:BNSH_REPO_URL) { $env:BNSH_REPO_URL } else { "https://github.com/binesheb/bnsh-ai.git" }
$InstallDir = if ($env:BNSH_INSTALL_DIR) { $env:BNSH_INSTALL_DIR } else { Join-Path (Get-Location) "bnsh-ai" }
$VenvDir = if ($env:BNSH_VENV) { $env:BNSH_VENV } else { Join-Path $InstallDir ".venv" }

Write-Host "[BNSH] Checking prerequisites..."

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git is required."
}

$python = Get-Command py -ErrorAction SilentlyContinue
if (-not $python) {
    $python = Get-Command python -ErrorAction SilentlyContinue
}
if (-not $python) {
    throw "Python 3.10+ is required."
}

$PythonCommand = $python.Source
$version = & $PythonCommand -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
& $PythonCommand -c "import sys; raise SystemExit(0 if sys.version_info >= (3,10) else 1)"
if ($LASTEXITCODE -ne 0) {
    throw "Python 3.10+ is required. Found $version."
}

if (-not (Test-Path (Join-Path $InstallDir ".git"))) {
    Write-Host "[BNSH] Cloning into $InstallDir..."
    git clone $RepoUrl $InstallDir
}

Set-Location $InstallDir

Write-Host "[BNSH] Creating virtual environment..."
& $PythonCommand -m venv $VenvDir

$VenvPython = Join-Path $VenvDir "Scripts\python.exe"

Write-Host "[BNSH] Installing BNSH AI..."
& $VenvPython -m pip install --upgrade pip
& $VenvPython -m pip install -e ".[dev]"

Write-Host "[BNSH] Running validation..."
& $VenvPython -m pytest -q

Write-Host ""
Write-Host "[BNSH] BNSH AI is ready."
Write-Host "Run:"
Write-Host "  $VenvDir\Scripts\Activate.ps1"
Write-Host "  bnsh health"
Write-Host '  bnsh chat "Hello from BNSH AI"'
