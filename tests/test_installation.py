from pathlib import Path
import hashlib
import json

from bnsh.installation import ModelInstaller, InstallStatus
from bnsh.model_catalog import ModelCatalog


def test_installation_rejects_unpublished_model(tmp_path):
    catalog = ModelCatalog(Path("models/catalog.json"))
    installer = ModelInstaller(catalog, tmp_path / "models")
    result = installer.install("ariv-1b")
    assert result.status is InstallStatus.FAILED
    assert "not installable" in result.message


def test_artifact_download_is_sha256_verified(tmp_path):
    artifact = tmp_path / "artifact.bin"
    artifact.write_bytes(b"bnsh-test")
    digest = hashlib.sha256(artifact.read_bytes()).hexdigest()

    catalog_path = tmp_path / "catalog.json"
    catalog_path.write_text(json.dumps({"models": [{
        "id": "test-model",
        "name": "Test",
        "family": "ARIV",
        "variant": "test",
        "status": "release",
        "description": "test",
        "tags": [],
        "artifacts": [{
            "uri": artifact.as_uri(),
            "filename": "weights.bin",
            "sha256": digest
        }]
    }]}), encoding="utf-8")

    result = ModelInstaller(ModelCatalog(catalog_path), tmp_path / "models").install("test-model")
    assert result.status is InstallStatus.INSTALLED
    assert (tmp_path / "models" / "test-model" / "weights.bin").read_bytes() == b"bnsh-test"


def test_bad_checksum_does_not_leave_weight_file(tmp_path):
    artifact = tmp_path / "artifact.bin"
    artifact.write_bytes(b"bnsh-test")

    catalog_path = tmp_path / "catalog.json"
    catalog_path.write_text(json.dumps({"models": [{
        "id": "test-model",
        "name": "Test",
        "family": "ARIV",
        "variant": "test",
        "status": "release",
        "description": "test",
        "tags": [],
        "artifacts": [{
            "uri": artifact.as_uri(),
            "filename": "weights.bin",
            "sha256": "0" * 64
        }]
    }]}), encoding="utf-8")

    try:
        ModelInstaller(ModelCatalog(catalog_path), tmp_path / "models").install("test-model")
    except ValueError as exc:
        assert "SHA-256" in str(exc)
    else:
        raise AssertionError("checksum failure should raise")
    assert not (tmp_path / "models" / "test-model" / "weights.bin").exists()
