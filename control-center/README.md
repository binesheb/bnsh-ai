# BNSH Control Center

The Control Center is the local web UI for BNSH AI and ARIV.

## First milestone

- Overview dashboard
- Model discovery
- Model status
- Install lifecycle
- Runtime status
- Hardware summary
- Activity/log surface

The UI is designed to consume the same model catalog and control API used by the CLI.

## Architecture

```
Browser
  ↓
Control Center UI
  ↓ HTTP/WebSocket
BNSH Control API
  ↓
Runtime / Model / Training / Learning managers
```

Future sections include Training, Evolution, Knowledge, Teachers, Evaluation, Hardware, and Settings.
