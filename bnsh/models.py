"""Local model registry and filesystem management."""
from dataclasses import dataclass
from pathlib import Path
import json
import shutil

@dataclass(frozen=True)
class ModelRecord:
    model_id: str
    path: Path
    revision: str | None = None
    source: str | None = None

class ModelManager:
    """Manage locally installed model directories without coupling to an inference engine."""

    def __init__(self, root: Path | None = None) -> None:
        self.root = root or Path.home() / ".bnsh" / "models"
        self.root.mkdir(parents=True, exist_ok=True)

    def list(self) -> list[ModelRecord]:
        records = []
        for directory in sorted(self.root.iterdir()):
            if not directory.is_dir():
                continue
            metadata = directory / "model.json"
            if not metadata.exists():
                continue
            data = json.loads(metadata.read_text(encoding="utf-8"))
            records.append(ModelRecord(
                model_id=directory.name,
                path=directory,
                revision=data.get("revision"),
                source=data.get("source"),
            ))
        return records

    def info(self, model_id: str) -> ModelRecord:
        path = self.root / model_id
        if not path.is_dir():
            raise FileNotFoundError(f"Model is not installed: {model_id}")
        metadata = path / "model.json"
        data = json.loads(metadata.read_text()) if metadata.exists() else {}
        return ModelRecord(model_id, path, data.get("revision"), data.get("source"))

    def register(self, model_id: str, source: str | None = None, revision: str | None = None) -> ModelRecord:
        path = self.root / model_id
        path.mkdir(parents=True, exist_ok=True)
        (path / "model.json").write_text(json.dumps({
            "model_id": model_id,
            "source": source,
            "revision": revision,
        }, indent=2) + "\n")
        return ModelRecord(model_id, path, revision, source)

    def remove(self, model_id: str) -> None:
        path = self.root / model_id
        if not path.is_dir():
            raise FileNotFoundError(f"Model is not installed: {model_id}")
        shutil.rmtree(path)
