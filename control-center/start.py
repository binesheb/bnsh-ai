"""Start the BNSH Control API and GUI."""
from __future__ import annotations
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
api = subprocess.Popen([sys.executable, str(ROOT / "backend" / "api.py")])
ui = subprocess.Popen([sys.executable, str(ROOT / "frontend" / "serve.py")])
try:
    for _ in range(30):
        if api.poll() is not None:
            raise SystemExit("BNSH Control API stopped during startup.")
        try:
            import urllib.request
            with urllib.request.urlopen("http://127.0.0.1:8790/api/health", timeout=0.25) as response:
                if response.status == 200:
                    break
        except Exception:
            time.sleep(0.1)
    else:
        raise SystemExit("BNSH Control API did not become ready.")
    webbrowser.open("http://127.0.0.1:8787")
    ui.wait()
finally:
    if ui.poll() is None:
        ui.terminate()
    if api.poll() is None:
        api.terminate()
