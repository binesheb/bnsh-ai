"""Local BNSH Control API."""
from __future__ import annotations

import json
import platform
import shutil
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runtime_service import RuntimeService

CATALOG = ROOT / "models" / "catalog.json"
RUNTIME = RuntimeService()
STARTED = time.time()


def catalog() -> dict:
    return json.loads(CATALOG.read_text(encoding="utf-8"))


def system_info() -> dict:
    disk = shutil.disk_usage(Path.home())
    try:
        import psutil
        memory = f"{psutil.virtual_memory().used / 1024**3:.1f} / {psutil.virtual_memory().total / 1024**3:.1f} GB"
        cpu_percent = psutil.cpu_percent(interval=0.05)
    except Exception:
        memory = "Unavailable"
        cpu_percent = None
    return {
        "platform": platform.platform(),
        "python": platform.python_version(),
        "cpu": platform.processor() or platform.machine(),
        "cpu_percent": cpu_percent,
        "memory": memory,
        "storage_free_gb": round(disk.free / 1024**3, 1),
        "uptime_seconds": round(time.time() - STARTED),
    }


class Handler(BaseHTTPRequestHandler):
    def _json(self, payload: dict, status: int = 200) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Access-Control-Allow-Origin", "http://127.0.0.1:8787")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _body(self) -> dict:
        length = int(self.headers.get("Content-Length", "0"))
        return json.loads(self.rfile.read(length) or b"{}")

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "http://127.0.0.1:8787")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        path = urlparse(self.path).path
        if path == "/api/chat":
            try:
                payload = self._body()
                return self._json(RUNTIME.chat(str(payload.get("message", ""))))
            except (ValueError, json.JSONDecodeError) as exc:
                return self._json({"ok": False, "error": "invalid_request", "message": str(exc)}, 400)
        return self._json({"error": "not_found"}, 404)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/api/health":
            return self._json({"status": "ok", "service": "bnsh-control-api"})
        if path == "/api/system":
            return self._json(system_info())
        if path == "/api/runtime":
            return self._json(RUNTIME.status())
        if path == "/api/models":
            return self._json(catalog())
        if path.startswith("/api/models/"):
            model_id = path.rsplit("/", 1)[-1]
            for model in catalog().get("models", []):
                if model["id"] == model_id:
                    return self._json({"model": model, "installed": False})
            return self._json({"error": "model_not_found"}, 404)
        if path == "/api/activity":
            return self._json({"items": [
                {"name": "Control API", "status": "Online"},
                {"name": "Model catalog", "status": "Loaded"},
                {"name": "ARIV runtime", "status": RUNTIME.status()["state"].title()},
            ]})
        return self._json({"error": "not_found"}, 404)

    def log_message(self, fmt, *args):
        return


def main() -> None:
    host = "127.0.0.1"
    port = 8790
    print(f"BNSH Control API: http://{host}:{port}")
    ThreadingHTTPServer((host, port), Handler).serve_forever()


if __name__ == "__main__":
    main()
