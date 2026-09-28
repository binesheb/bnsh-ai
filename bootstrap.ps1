# BNSH AI Bootstrap Installer
# Usage: irm https://raw.githubusercontent.com/binesheb/bnsh-ai/main/bootstrap.ps1 | iex
$ErrorActionPreference = "Stop"
$Repo = "https://github.com/binesheb/bnsh-ai.git"
$InstallRoot = Join-Path $env:LOCALAPPDATA "BNSH"
$RepoRoot = Join-Path $InstallRoot "bnsh-ai"
$Launcher = Join-Path $InstallRoot "bnsh.ps1"
function Require-Command($Name, $InstallHint) { if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) { throw "$Name is required. $InstallHint" } }
Write-Host "  BNSH AI Bootstrap" -ForegroundColor Cyan
Require-Command "git" "Install Git for Windows, then run this command again."
Require-Command "python" "Install Python 3.11+ and ensure it is on PATH."
New-Item -ItemType Directory -Force -Path $InstallRoot | Out-Null
if (Test-Path (Join-Path $RepoRoot ".git")) { git -C $RepoRoot pull --ff-only } else { git clone $Repo $RepoRoot }
$Venv = Join-Path $InstallRoot ".venv"
if (-not (Test-Path (Join-Path $Venv "Scripts\python.exe"))) { python -m venv $Venv }
$Python = Join-Path $Venv "Scripts\python.exe"
& $Python -m pip install --upgrade pip
$Requirements = Join-Path $RepoRoot "requirements.txt"
if (Test-Path $Requirements) { & $Python -m pip install -r $Requirements }
$launcherContent = 'Set-Item Env:BNSH_HOME "' + $InstallRoot + '"' + [Environment]::NewLine + 'Set-Item Env:BNSH_REPO "' + $RepoRoot + '"' + [Environment]::NewLine + '& "' + $Python + '" -m bnsh.cli $args' + [Environment]::NewLine
$launcherContent | Set-Content -Encoding UTF8 $Launcher
$Control = Join-Path $InstallRoot "control-center.ps1"
$controlContent = 'Set-Location "' + $RepoRoot + '\control-center\frontend"' + [Environment]::NewLine + '& "' + $Python + '" serve.py' + [Environment]::NewLine
$controlContent | Set-Content -Encoding UTF8 $Control
Write-Host "BNSH AI installed." -ForegroundColor Green
Write-Host ("CLI launcher: " + $Launcher) -ForegroundColor Cyan
Write-Host ("Control Center launcher: " + $Control) -ForegroundColor Cyan