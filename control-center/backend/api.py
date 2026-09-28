"""Local BNSH Control API.

The API is intentionally dependency-light for the first milestone.
Run with:
    python control-center/backend/api.py
"""
from __future__ import annotations

import json
import os
import platform
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "models" / "catalog.json"
STARTED = time.time()


def catalog() -> dict:
    return json.loads(CATALOG.read_text(encoding="utf-8"))


def system_info() -> dict:
    try:
        import shutil
        disk = shutil.disk_usage(Path.home())
        storage_free_gb = round(disk.free / 1024**3, 1)
    except Exception:
        storage_free_gb = None
    return {
        "platform": platform.platform(),
        "python": platform.python_version(),
        "cpu": platform.processor() or platform.machine(),
        "memory": _memory(),
        "storage_free_gb": storage_free_gb,
        "uptime_seconds": round(time.time() - STARTED),
    }


def _memory() -> str:
    try:
        import psutil
        return f"{psutil.virtual_memory().used / 1024**3:.1f} / {psutil.virtual_memory().total / 1024**3:.1f} GB"
    except Exception:
        return "Unavailable"


class Handler(BaseHTTPRequestHandler):
    def _json(self, payload: dict, status: int = 200) -> None:
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "http://127.0.0.1:8787")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "http://127.0.0.1:8787")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/api/health":
            return self._json({"status": "ok", "service": "bnsh-control-api"})
        if path == "/api/system":
            return self._json(system_info())
        if path == "/api/models":
            return self._json(catalog())
        if path.startswith("/api/models/"):
            model_id = path.rsplit("/", 1)[-1]
            for model in catalog().get("models", []):
                if model["id"] == model_id:
                    return self._json({"model": model, "installed": False})
            return self._json({"error": "model_not_found"}, 404)
        if path == "/api/activity":
            return self._json({
                "items": [
                    {"name": "Control API", "status": "Online"},
                    {"name": "Model catalog", "status": "Loaded"},
                    {"name": "ARIV runtime", "status": "Not started"},
                ]
            })
        return self._json({"error": "not_found"}, 404)

    def log_message(self, fmt, *args):
        return


def main() -> None:
    host = os.getenv("BNSH_CONTROL_HOST", "127.0.0.1")
    port = int(os.getenv("BNSH_CONTROL_PORT", "8790"))
    print(f"BNSH Control API: http://{host}:{port}")
    ThreadingHTTPServer((host, port), Handler).serve_forever()


if __name__ == "__main__":
    main()
