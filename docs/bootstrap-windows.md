# BNSH Windows IRM Bootstrap

One-command installation:

```powershell
irm https://raw.githubusercontent.com/binesheb/bnsh-ai/main/bootstrap.ps1 | iex
```

Installs or updates BNSH into `%LOCALAPPDATA%\BNSH`, creates an isolated Python environment, and creates CLI and Control Center launchers.

It is safe to rerun and does not automatically download large ARIV model weights.

Control Center:

```powershell
powershell -ExecutionPolicy Bypass -File "$env:LOCALAPPDATA\BNSH\control-center.ps1"
```

Then open `http://127.0.0.1:8787`.