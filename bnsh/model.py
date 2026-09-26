"""Model metadata and loading contracts."""
from dataclasses import dataclass

@dataclass(frozen=True)
class ModelInfo:
    id: str
    architecture: str | None = None
    parameter_count: int | None = None
    context_length: int | None = None
    languages: tuple[str, ...] = ()
    modality: str = "text"
    revision: str | None = None
    license: str | None = None
