# BNSH Control Center

The Control Center is the local GUI for monitoring and controlling BNSH AI.

## Start

After the Windows bootstrap:

    bnsh control

The launcher starts the local API and browser GUI and opens http://127.0.0.1:8787.

## Safety

The Control Center binds to loopback only by default. It is not an internet-facing server.

The GUI is intended to control local model installation, runtime state, inference, system monitoring, activity/logs, and future training/evaluation/evolution jobs.

The API is separate from the UI so BINESH OS and other clients can use the same control layer.
