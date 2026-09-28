import subprocess,sys,time,webbrowser
from pathlib import Path
ROOT=Path(__file__).resolve().parent
api=subprocess.Popen([sys.executable,str(ROOT/"backend/api.py")])
ui=subprocess.Popen([sys.executable,str(ROOT/"frontend/serve.py")])
time.sleep(.8); webbrowser.open("http://127.0.0.1:8787")
try: ui.wait()
finally: api.terminate()
