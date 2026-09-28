"""Start the local BNSH Control API and Control Center."""
from __future__ import annotations
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
backend = ROOT / "backend" / "api.py"
frontend = ROOT / "frontend" / "serve.py"

api = subprocess.Popen([sys.executable, str(backend)])
ui = subprocess.Popen([sys.executable, str(frontend)])
time.sleep(0.8)
webbrowser.open("http://127.0.0.1:8787")
try:
    ui.wait()
finally:
    api.terminate()
