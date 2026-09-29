"""BNSH command-line interface."""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

from .model_catalog import ModelCatalog
from .runtime.facade import BNSHRuntime

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "models" / "catalog.json"
CONTROL_CENTER = ROOT / "control-center" / "start.py"


def open_control_center() -> None:
    if not CONTROL_CENTER.exists():
        raise SystemExit("Control Center is not installed in this checkout.")
    os.chdir(CONTROL_CENTER.parent)
    subprocess.run([sys.executable, str(CONTROL_CENTER)], check=True)


def doctor() -> int:
    checks = []
    checks.append(("Python", sys.version.split()[0]))
    checks.append(("BNSH package", "ok"))
    checks.append(("Model catalog", "ok" if CATALOG.exists() else "missing"))
    checks.append(("Control Center", "ok" if CONTROL_CENTER.exists() else "missing"))
    for name, value in checks:
        print(f"{name}: {value}")
    return 0 if all(value not in {"missing"} for _, value in checks) else 1


def main() -> None:
    parser = argparse.ArgumentParser(prog="bnsh")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("control", help="Start the local BNSH Control Center")
    sub.add_parser("doctor", help="Check the local BNSH installation")
    sub.add_parser("health", help="Check basic BNSH installation health")

    chat = sub.add_parser("chat", help="Send a message to the development runtime")
    chat.add_argument("message")

    model = sub.add_parser("model", help="Manage ARIV models")
    model_sub = model.add_subparsers(dest="model_command")
    model_sub.add_parser("list")
    info = model_sub.add_parser("info")
    info.add_argument("model_id")

    args = parser.parse_args()

    if args.command == "control":
        open_control_center()
        return
    if args.command in {"doctor", "health"}:
        raise SystemExit(doctor())
    if args.command == "chat":
        print(BNSHRuntime(model="development").chat(args.message))
        return
    if args.command == "model" and args.model_command == "list":
        for item in ModelCatalog(CATALOG).list():
            print(f"{item.id}\t{item.status}\t{item.description}")
        return
    if args.command == "model" and args.model_command == "info":
        item = ModelCatalog(CATALOG).get(args.model_id)
        print(f"Name: {item.name}")
        print(f"Family: {item.family}")
        print(f"Variant: {item.variant}")
        print(f"Status: {item.status}")
        print(f"Description: {item.description}")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
