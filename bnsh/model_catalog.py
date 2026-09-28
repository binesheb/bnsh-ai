"""ARIV model catalog and installation metadata."""
from dataclasses import dataclass
import json
from pathlib import Path

@dataclass(frozen=True)
class ModelArtifact:
    uri: str
    filename: str
    size_bytes: int | None = None
    sha256: str | None = None

@dataclass(frozen=True)
class ModelEntry:
    id: str
    name: str
    family: str
    variant: str
    status: str
    description: str
    tags: tuple[str, ...]
    artifacts: tuple[ModelArtifact, ...]

class ModelCatalog:
    def __init__(self, path: str | Path):
        self.path = Path(path)

    def list(self) -> list[ModelEntry]:
        payload = json.loads(self.path.read_text(encoding="utf-8"))
        return [self._entry(item) for item in payload.get("models", [])]

    def get(self, model_id: str) -> ModelEntry:
        for model in self.list():
            if model.id == model_id:
                return model
        raise KeyError(f"Unknown model: {model_id}")

    @staticmethod
    def _entry(item: dict) -> ModelEntry:
        artifacts = tuple(
            ModelArtifact(
                uri=a["uri"],
                filename=a["filename"],
                size_bytes=a.get("size_bytes"),
                sha256=a.get("sha256"),
            )
            for a in item.get("artifacts", [])
        )
        return ModelEntry(
            id=item["id"],
            name=item["name"],
            family=item["family"],
            variant=item["variant"],
            status=item["status"],
            description=item["description"],
            tags=tuple(item.get("tags", [])),
            artifacts=artifacts,
        )
