"""Model installation lifecycle for BNSH AI."""
from __future__ import annotations

import hashlib
import json
import os
import tempfile
import urllib.request
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
        self.models_dir.mkdir(parents=True, exist_ok=True)

    def status(self, model_id: str) -> InstallResult:
        model = self.catalog.get(model_id)
        target = self.models_dir / model.id
        if (target / "model.json").exists():
            return InstallResult(model.id, InstallStatus.INSTALLED, str(target))
        return InstallResult(model.id, InstallStatus.AVAILABLE)

    def install(self, model_id: str) -> InstallResult:
        model = self.catalog.get(model_id)
        if model.status not in {"available", "release"}:
            return InstallResult(model.id, InstallStatus.FAILED,
                                 message=f"Model is not installable yet: {model.status}.")
        if not model.artifacts:
            return InstallResult(model.id, InstallStatus.FAILED,
                                 message="No release artifact is published for this model yet.")

        target = self.models_dir / model.id
        target.mkdir(parents=True, exist_ok=True)

        for artifact in model.artifacts:
            filename = Path(artifact.filename).name
            if not filename or filename in {".", ".."}:
                raise ValueError("Invalid model artifact filename.")
            destination = target / filename
            self._download_and_verify(artifact.uri, destination, artifact.sha256)

        metadata = {
            "model_id": model.id,
            "name": model.name,
            "family": model.family,
            "variant": model.variant,
            "source": "BNSH Model Hub",
            "files": [Path(a.filename).name for a in model.artifacts],
        }
        (target / "model.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
        return InstallResult(model.id, InstallStatus.INSTALLED, str(target))

    @staticmethod
    def _download_and_verify(uri: str, destination: Path, expected_sha256: str | None) -> None:
        temp_fd, temp_name = tempfile.mkstemp(prefix=destination.name + ".", dir=destination.parent)
        os.close(temp_fd)
        temp = Path(temp_name)
        digest = hashlib.sha256()
        try:
            with urllib.request.urlopen(uri, timeout=60) as response, temp.open("wb") as output:
                while True:
                    chunk = response.read(1024 * 1024)
                    if not chunk:
                        break
                    output.write(chunk)
                    digest.update(chunk)
            if expected_sha256 and digest.hexdigest().lower() != expected_sha256.lower():
                raise ValueError(f"SHA-256 verification failed for {destination.name}.")
            temp.replace(destination)
        finally:
            temp.unlink(missing_ok=True)
