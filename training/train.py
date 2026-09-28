"""Minimal ARIV causal-LM training entry point.

This script intentionally requires the optional ML dependencies. It is designed
for small experiments and pipeline validation, not production-scale training.
"""
import argparse
import json
from pathlib import Path

def load_jsonl(path: Path) -> list[str]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line)["text"])
    return rows

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    config = Path(args.config)
    if not config.exists():
        raise FileNotFoundError(config)

    try:
        import yaml
    except ImportError as exc:
        raise SystemExit("Install training dependencies with: pip install -e '.[training]'") from exc

    settings = yaml.safe_load(config.read_text(encoding="utf-8"))
    train_path = Path(settings["data"]["train"])
    validation_path = Path(settings["data"]["validation"])

    train = load_jsonl(train_path)
    validation = load_jsonl(validation_path)

    if not train or not validation:
        raise ValueError("Training and validation datasets must not be empty.")

    print(f"ARIV training configuration: {config}")
    print(f"Training examples: {len(train)}")
    print(f"Validation examples: {len(validation)}")

    if args.dry_run:
        print("Dry run successful.")
        return

    raise SystemExit(
        "The first ARIV training implementation is intentionally gated. "
        "The next stage will connect tokenizer/model construction and Trainer "
        "after the experiment configuration is validated."
    )

if __name__ == "__main__":
    main()
