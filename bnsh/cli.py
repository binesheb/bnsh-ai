"""Command-line interface for BNSH AI development and model management."""
import argparse

from .backends import EchoBackend
from .models import ModelManager
from .runtime import BNSHRuntime

def main() -> None:
    parser = argparse.ArgumentParser(prog="bnsh")
    sub = parser.add_subparsers(dest="command")

    health = sub.add_parser("health")
    health.add_argument("--model", default=None)

    chat = sub.add_parser("chat")
    chat.add_argument("prompt")
    chat.add_argument("--model", default=None)

    model = sub.add_parser("model")
    model_sub = model.add_subparsers(dest="model_command")
    model_sub.add_parser("list")
    info = model_sub.add_parser("info")
    info.add_argument("model_id")
    register = model_sub.add_parser("register")
    register.add_argument("model_id")
    register.add_argument("--source", default=None)
    register.add_argument("--revision", default=None)
    remove = model_sub.add_parser("remove")
    remove.add_argument("model_id")

    args = parser.parse_args()

    if args.command == "health":
        print(BNSHRuntime(model=args.model, backend=EchoBackend()).health())
    elif args.command == "chat":
        print(BNSHRuntime(model=args.model, backend=EchoBackend()).chat(args.prompt))
    elif args.command == "model":
        manager = ModelManager()
        if args.model_command == "list":
            for record in manager.list():
                print(f"{record.model_id}\t{record.revision or '-'}\t{record.source or '-'}")
        elif args.model_command == "info":
            record = manager.info(args.model_id)
            print({
                "model_id": record.model_id,
                "path": str(record.path),
                "revision": record.revision,
                "source": record.source,
            })
        elif args.model_command == "register":
            record = manager.register(args.model_id, args.source, args.revision)
            print(f"Registered {record.model_id} at {record.path}")
        elif args.model_command == "remove":
            manager.remove(args.model_id)
            print(f"Removed {args.model_id}")
        else:
            model.print_help()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
