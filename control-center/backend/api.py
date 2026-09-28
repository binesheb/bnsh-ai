import json, os, platform, sys, time, shutil
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from bnsh.runtime.base import ChatMessage, GenerationConfig, RuntimeNotReady
from bnsh.runtime.manager import RuntimeManager
from bnsh.runtime.mock import MockARIVProvider
CATALOG=ROOT/"models/catalog.json"; RUNTIME=RuntimeManager(); STARTED=time.time()
def catalog(): return json.loads(CATALOG.read_text(encoding="utf-8"))
def system_info():
    d=shutil.disk_usage(Path.home())
    try:
        import psutil
        mem=f"{psutil.virtual_memory().used/1024**3:.1f} / {psutil.virtual_memory().total/1024**3:.1f} GB"
    except Exception: mem="Unavailable"
    return {"platform":platform.platform(),"python":platform.python_version(),"cpu":platform.processor() or platform.machine(),"memory":mem,"storage_free_gb":round(d.free/1024**3,1),"uptime_seconds":round(time.time()-STARTED)}
class Handler(BaseHTTPRequestHandler):
    def out(self,p,status=200):
        b=json.dumps(p).encode(); self.send_response(status); self.send_header("Content-Type","application/json"); self.send_header("Content-Length",str(len(b))); self.send_header("Access-Control-Allow-Origin","http://127.0.0.1:8787"); self.end_headers(); self.wfile.write(b)
    def body(self):
        return json.loads(self.rfile.read(int(self.headers.get("Content-Length","0"))) or b"{}")
    def do_OPTIONS(self):
        self.send_response(204); self.send_header("Access-Control-Allow-Origin","http://127.0.0.1:8787"); self.send_header("Access-Control-Allow-Methods","GET, POST, OPTIONS"); self.end_headers()
    def do_GET(self):
        p=urlparse(self.path).path
        if p=="/api/health": return self.out({"status":"ok","service":"bnsh-control-api"})
        if p=="/api/system": return self.out(system_info())
        if p=="/api/runtime": return self.out({"ready":RUNTIME.ready,"model_id":RUNTIME.model_id,"provider":RUNTIME.provider})
        if p=="/api/models": return self.out(catalog())
        if p=="/api/activity": return self.out({"items":[{"name":"Control API","status":"Online"},{"name":"Model catalog","status":"Loaded"},{"name":"ARIV runtime","status":"Ready" if RUNTIME.ready else "Not started"}]})
        return self.out({"error":"not_found"},404)
    def do_POST(self):
        p=urlparse(self.path).path; data=self.body()
        if p=="/api/runtime/load":
            mid=data.get("model_id")
            if not mid: return self.out({"error":"model_id_required"},400)
            RUNTIME.load(mid,MockARIVProvider())
            return self.out({"status":"ok","model_id":mid,"provider":RUNTIME.provider,"development_mode":True})
        if p=="/api/chat":
            try:
                msgs=[ChatMessage(str(x.get("role","user")),str(x.get("content",""))) for x in data.get("messages",[])]
                if not msgs: return self.out({"error":"messages_required"},400)
                ans=RUNTIME.generate(msgs,GenerationConfig(float(data.get("temperature",.7)),int(data.get("max_tokens",512)),float(data.get("top_p",.9))))
                return self.out({"model":RUNTIME.model_id,"provider":RUNTIME.provider,"message":{"role":"assistant","content":ans},"development_mode":RUNTIME.provider=="mock"})
            except RuntimeNotReady as e: return self.out({"error":"runtime_not_ready","message":str(e)},409)
        return self.out({"error":"not_found"},404)
    def log_message(self,*args): pass
def main():
    host=os.getenv("BNSH_CONTROL_HOST","127.0.0.1"); port=int(os.getenv("BNSH_CONTROL_PORT","8790"))
    print(f"BNSH Control API: http://{host}:{port}"); ThreadingHTTPServer((host,port),Handler).serve_forever()
if __name__=="__main__": main()
