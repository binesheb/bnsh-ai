"""Local Control Center static server."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
server = ThreadingHTTPServer(("127.0.0.1", 8787), SimpleHTTPRequestHandler)
print("BNSH Control Center: http://127.0.0.1:8787")
server.serve_forever()
