"""Command-line interface for BNSH AI development."""
import argparse
from .backends import EchoBackend
from .runtime import BNSHRuntime

def main() -> None:
    parser = argparse.ArgumentParser(prog="bnsh")
    sub = parser.add_subparsers(dest="command")
    health = sub.add_parser("health")
    health.add_argument("--model", default=None)
    chat = sub.add_parser("chat")
    chat.add_argument("prompt")
    chat.add_argument("--model", default=None)
    args = parser.parse_args()

    if args.command == "health":
        print(BNSHRuntime(model=args.model, backend=EchoBackend()).health())
    elif args.command == "chat":
        print(BNSHRuntime(model=args.model, backend=EchoBackend()).chat(args.prompt))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
