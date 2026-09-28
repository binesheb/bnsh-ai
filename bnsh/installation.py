"""Safe model installation lifecycle.

Actual network downloads are intentionally delegated to a future download
backend. This layer owns state, validation, and lifecycle semantics.
"""
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from .model_catalog import ModelCatalog, ModelEntry

class InstallStatus(str, Enum):
    AVAILABLE = "available"
    DOWNLOADING = "downloading"
    INSTALLED = "installed"
    FAILED = "failed"

@dataclass(frozen=True)
class InstallResult:
    model_id: str
    status: InstallStatus
    location: str | None = None
    message: str = ""

class ModelInstaller:
    def __init__(self, catalog: ModelCatalog, models_dir: str | Path):
        self.catalog = catalog
        self.models_dir = Path(models_dir)

    def status(self, model_id: str) -> InstallResult:
        model = self.catalog.get(model_id)
        target = self.models_dir / model.id
        if target.exists():
            return InstallResult(model.id, InstallStatus.INSTALLED, str(target))
        return InstallResult(model.id, InstallStatus.AVAILABLE)

    def install(self, model_id: str) -> InstallResult:
        model = self.catalog.get(model_id)
        if model.status not in {"available", "release"}:
            return InstallResult(
                model.id,
                InstallStatus.FAILED,
                message=f"Model is not installable yet: {model.status}",
            )
        if not model.artifacts:
            return InstallResult(
                model.id,
                InstallStatus.FAILED,
                message="No release artifact is published for this model yet.",
            )
        target = self.models_dir / model.id
        target.mkdir(parents=True, exist_ok=True)
        return InstallResult(
            model.id,
            InstallStatus.DOWNLOADING,
            str(target),
            "Download backend not connected yet.",
        )
