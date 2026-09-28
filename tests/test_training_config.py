import json
from pathlib import Path

from training.train import load_jsonl

def test_sample_training_data():
    rows = load_jsonl(Path("data/sample/train.jsonl"))
    assert len(rows) == 3
    assert all(isinstance(row, str) and row for row in rows)

def test_dataset_manifest_schema_exists():
    schema = json.loads(Path("data/dataset.schema.json").read_text())
    assert schema["title"] == "ARIV Dataset Manifest"
    assert "license" in schema["required"]
