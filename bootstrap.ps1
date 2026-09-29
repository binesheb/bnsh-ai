# BNSH AI Windows field installer
# Usage:
#   irm https://raw.githubusercontent.com/binesheb/bnsh-ai/main/bootstrap.ps1 | iex
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

function Ensure-Prerequisite($command, $wingetId, $name) {
    if (Get-Command $command -ErrorAction SilentlyContinue) { return }
    if (Get-Command winget -ErrorAction SilentlyContinue) {
        Step "Installing $name with Windows Package Manager..."
        winget install --id $wingetId --exact --accept-package-agreements --accept-source-agreements --silent
        Refresh-Path
    }
    if (-not (Get-Command $command -ErrorAction SilentlyContinue)) {
        Fail "$name is required. Install it and run the bootstrap again."
    }
}

Step "Checking Windows prerequisites"
Ensure-Prerequisite "git" "Git.Git" "Git for Windows"
Ensure-Prerequisite "python" "Python.Python.3.11" "Python 3.11"

New-Item -ItemType Directory -Force -Path $InstallRoot | Out-Null

if (Test-Path (Join-Path $RepoRoot ".git")) {
    Step "Updating BNSH source"
    git -C $RepoRoot pull --ff-only
} else {
    Step "Downloading BNSH source"
    git clone $Repo $RepoRoot
}

Step "Creating isolated Python environment"
if (-not (Test-Path $Python)) {
    python -m venv $Venv
}
if (-not (Test-Path $Python)) { Fail "Python virtual environment creation failed." }

Step "Installing BNSH and Control Center dependencies"
& $Python -m pip install --upgrade pip
& $Python -m pip install -e "${RepoRoot}[dev]"

if ($LASTEXITCODE -ne 0) { Fail "BNSH installation failed." }

Step "Activating BNSH in this PowerShell session"
if ($env:Path -notlike "*$Bin*") { $env:Path = "$Bin;$env:Path" }

$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
$parts = @($userPath -split ";" | Where-Object { $_ -and $_ -ne $Bin })
[Environment]::SetEnvironmentVariable("Path", (($parts + $Bin) -join ";"), "User")

$launcher = Join-Path $InstallRoot "bnsh-control.ps1"
@"
& "$Python" -m bnsh.cli control
"@ | Set-Content -Encoding UTF8 $launcher

Step "Validating installation"
& $Python -m bnsh.cli model list
if ($LASTEXITCODE -ne 0) { Fail "BNSH CLI validation failed." }

Write-Host ""
Write-Host "BNSH AI is installed and ready." -ForegroundColor Green
Write-Host ""
Write-Host "Start the GUI now:" -ForegroundColor Yellow
Write-Host "  bnsh control" -ForegroundColor White
Write-Host ""
Write-Host "If 'bnsh' is not recognized in an already-open terminal, open a new PowerShell window." -ForegroundColor DarkGray
