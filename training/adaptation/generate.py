"""Generate a teacher-labelled JSONL adaptation dataset."""
import argparse
import json
from pathlib import Path

from .teacher import Teacher

def generate_dataset(
    prompts: list[str],
    teacher: Teacher,
    output: Path,
) -> int:
    output.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with output.open("w", encoding="utf-8") as handle:
        for prompt in prompts:
            if not prompt.strip():
                continue
            response = teacher.generate(prompt)
            record = {
                "prompt": prompt,
                "response": response,
                "teacher": {
                    "id": teacher.info.id,
                    "revision": teacher.info.revision,
                },
            }
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
            count += 1
    return count

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompts", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    prompts = [
        line.strip()
        for line in Path(args.prompts).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    raise SystemExit(
        "Use generate_dataset() from an adapter implementation. "
        "No external model is invoked by this command yet."
    )

if __name__ == "__main__":
    main()
