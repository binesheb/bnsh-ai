#!/usr/bin/env bash
set -euo pipefail

# BNSH AI bootstrap installer.
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/binesheb/bnsh-ai/main/bootstrap.sh | bash
#   ./bootstrap.sh
#
# Optional:
#   BNSH_INSTALL_DIR=/path/to/project ./bootstrap.sh

REPO_URL="${BNSH_REPO_URL:-https://github.com/binesheb/bnsh-ai.git}"
INSTALL_DIR="${BNSH_INSTALL_DIR:-$PWD/bnsh-ai}"
PYTHON_BIN="${BNSH_PYTHON:-python3}"
VENV_DIR="${BNSH_VENV:-$INSTALL_DIR/.venv}"

log() { printf '\n[BNSH] %s\n' "$1"; }
fail() { printf '\n[BNSH] ERROR: %s\n' "$1" >&2; exit 1; }

command -v git >/dev/null 2>&1 || fail "Git is required."
command -v "$PYTHON_BIN" >/dev/null 2>&1 || fail "Python 3 is required."

PY_VERSION="$("$PYTHON_BIN" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
"$PYTHON_BIN" -c 'import sys; raise SystemExit(0 if sys.version_info >= (3,10) else 1)'   || fail "Python 3.10 or newer is required. Found $PY_VERSION."

if [ ! -d "$INSTALL_DIR/.git" ]; then
  log "Cloning BNSH AI into $INSTALL_DIR"
  mkdir -p "$(dirname "$INSTALL_DIR")"
  git clone "$REPO_URL" "$INSTALL_DIR"
else
  log "Using existing BNSH AI checkout"
fi

cd "$INSTALL_DIR"

log "Creating Python virtual environment"
"$PYTHON_BIN" -m venv "$VENV_DIR"

# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

log "Installing BNSH AI"
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"

log "Running validation"
pytest -q

log "BNSH AI is ready"
printf '\nRun:\n  source "%s/bin/activate"\n  bnsh health\n  bnsh chat "Hello from BNSH AI"\n\n' "$VENV_DIR"
