from pathlib import Path

from bnsh.model_catalog import ModelCatalog

def test_catalog_contains_ariv_models():
    catalog = ModelCatalog(Path("models/catalog.json"))
    ids = {model.id for model in catalog.list()}
    assert "ariv-1b" in ids
    assert "ariv-3b" in ids
    assert "ariv-instruct" in ids

def test_catalog_identity():
    model = ModelCatalog(Path("models/catalog.json")).get("ariv-3b")
    assert model.family == "ARIV"
    assert model.variant == "base"
