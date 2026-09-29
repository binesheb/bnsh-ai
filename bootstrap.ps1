# BNSH AI Windows field installer
# Usage: irm https://raw.githubusercontent.com/binesheb/bnsh-ai/main/bootstrap.ps1 | iex
$ErrorActionPreference = "Stop"

$Repo = "https://github.com/binesheb/bnsh-ai.git"
$InstallRoot = Join-Path $env:LOCALAPPDATA "BNSH"
$RepoRoot = Join-Path $InstallRoot "bnsh-ai"
$Venv = Join-Path $InstallRoot ".venv"
$Python = Join-Path $Venv "Scripts\python.exe"
$Bin = Join-Path $Venv "Scripts"

function Step($message) { Write-Host "[BNSH] $message" -ForegroundColor Cyan }
function Fail($message) { throw "[BNSH] $message" }
function Refresh-Path {
  $machine = [Environment]::GetEnvironmentVariable("Path", "Machine")
  $user = [Environment]::GetEnvironmentVariable("Path", "User")
  $env:Path = "$machine;$user"
}

function Get-SupportedPython {
  $paths = @()
  if (Get-Command py -ErrorAction SilentlyContinue) {
    foreach ($minor in @("13","12","11")) {
      try { $p = (& py "-3.$minor" -c "import sys; print(sys.executable)" 2>$null).Trim(); if ($p) { $paths += $p } } catch {}
    }
  }
  if (Get-Command python -ErrorAction SilentlyContinue) {
    try { $p = (& python -c "import sys; print(sys.executable)" 2>$null).Trim(); if ($p) { $paths += $p } } catch {}
  }
  foreach ($path in $paths) {
    try { $version = (& $path -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>$null).Trim(); if ($version -match '^3\.(11|12|13)$') { return $path } } catch {}
  }
  return $null
}

function Ensure-Git {
  if (Get-Command git -ErrorAction SilentlyContinue) { return }
  if (Get-Command winget -ErrorAction SilentlyContinue) {
    Step "Installing Git for Windows..."
    winget install --id Git.Git --exact --accept-package-agreements --accept-source-agreements --silent
    Refresh-Path
  }
  if (-not (Get-Command git -ErrorAction SilentlyContinue)) { Fail "Git for Windows is required and could not be installed automatically." }
}

function Ensure-Python {
  $resolved = Get-SupportedPython
  if ($resolved) { return $resolved }
  if (-not (Get-Command winget -ErrorAction SilentlyContinue)) { Fail "Python 3.11, 3.12, or 3.13 is required and winget is unavailable." }
  Step "Installing Python 3.13..."
  winget install --id Python.Python.3.13 --exact --accept-package-agreements --accept-source-agreements --silent
  Refresh-Path
  $resolved = Get-SupportedPython
  if (-not $resolved) { Fail "Python 3.13 installation completed but no supported Python interpreter was found." }
  return $resolved
}

Step "Checking Windows prerequisites"
Ensure-Git
$SystemPython = Ensure-Python
Step "Using Python: $SystemPython"
New-Item -ItemType Directory -Force -Path $InstallRoot | Out-Null

if (Test-Path $RepoRoot) {
  if (-not (Test-Path (Join-Path $RepoRoot ".git"))) { Fail "Existing installation directory is not a Git checkout: $RepoRoot" }
  Step "Updating BNSH source"
  git -C $RepoRoot pull --ff-only
  if ($LASTEXITCODE -ne 0) { Fail "Could not update the existing BNSH checkout with a fast-forward pull." }
} else {
  Step "Downloading BNSH source"
  git clone $Repo $RepoRoot
  if ($LASTEXITCODE -ne 0) { Fail "Could not clone the BNSH repository." }
}

Step "Creating isolated Python environment"
if (-not (Test-Path $Python)) { & $SystemPython -m venv $Venv; if ($LASTEXITCODE -ne 0) { Fail "Python virtual environment creation failed." } }
if (-not (Test-Path $Python)) { Fail "Python virtual environment was not created." }

Step "Installing BNSH and Control Center dependencies"
& $Python -m pip install --upgrade pip
if ($LASTEXITCODE -ne 0) { Fail "pip upgrade failed." }
& $Python -m pip install -e "${RepoRoot}[dev]"
if ($LASTEXITCODE -ne 0) { Fail "BNSH installation failed." }

Step "Validating installation"
& $Python -m bnsh.cli doctor
if ($LASTEXITCODE -ne 0) { Fail "BNSH installation validation failed." }
& $Python -m bnsh.cli model list
if ($LASTEXITCODE -ne 0) { Fail "BNSH model catalog validation failed." }

if ($env:Path -notlike "*$Bin*") { $env:Path = "$Bin;$env:Path" }
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
$parts = @($userPath -split ";" | Where-Object { $_ -and $_ -ne $Bin })
[Environment]::SetEnvironmentVariable("Path", (($parts + $Bin) -join ";"), "User")
Write-Host ""
Write-Host "BNSH AI is installed and ready." -ForegroundColor Green
Write-Host "Start the GUI with: bnsh control" -ForegroundColor Yellow
Write-Host "Run diagnostics with: bnsh doctor" -ForegroundColor Yellow
Write-Host "Open a new PowerShell window if bnsh is not recognized here." -ForegroundColor DarkGray