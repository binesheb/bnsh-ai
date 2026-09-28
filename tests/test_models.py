from pathlib import Path
import pytest

from bnsh.models import ModelManager

def test_register_list_info_remove(tmp_path: Path):
    manager = ModelManager(tmp_path / "models")
    manager.register("demo", source="local", revision="v1")

    records = manager.list()
    assert len(records) == 1
    assert records[0].model_id == "demo"

    record = manager.info("demo")
    assert record.source == "local"
    assert record.revision == "v1"

    manager.remove("demo")
    assert manager.list() == []

def test_missing_model(tmp_path: Path):
    manager = ModelManager(tmp_path / "models")
    with pytest.raises(FileNotFoundError):
        manager.info("missing")
