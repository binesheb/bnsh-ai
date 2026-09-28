"""BNSH command-line interface."""
import argparse
from pathlib import Path

from .model_catalog import ModelCatalog

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "models" / "catalog.json"

def main() -> None:
    parser = argparse.ArgumentParser(prog="bnsh")
    sub = parser.add_subparsers(dest="command")

    model = sub.add_parser("model")
    model_sub = model.add_subparsers(dest="model_command")
    model_sub.add_parser("list")
    info = model_sub.add_parser("info")
    info.add_argument("model_id")

    args = parser.parse_args()

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
