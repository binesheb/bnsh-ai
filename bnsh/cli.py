"""BNSH command-line interface."""
import argparse
import os
import subprocess
import sys
from pathlib import Path

from .model_catalog import ModelCatalog

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "models" / "catalog.json"
CONTROL_CENTER = ROOT / "control-center" / "frontend" / "serve.py"


def open_control_center() -> None:
    """Start the local Control Center."""
    if not CONTROL_CENTER.exists():
        raise SystemExit("Control Center is not installed in this checkout.")
    os.chdir(CONTROL_CENTER.parent)
    subprocess.run([sys.executable, str(CONTROL_CENTER)], check=True)


def main() -> None:
    parser = argparse.ArgumentParser(prog="bnsh")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("control", help="Start the local BNSH Control Center")

    model = sub.add_parser("model", help="Manage ARIV models")
    model_sub = model.add_subparsers(dest="model_command")
    model_sub.add_parser("list")
    info = model_sub.add_parser("info")
    info.add_argument("model_id")

    args = parser.parse_args()

    if args.command == "control":
        open_control_center()
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
