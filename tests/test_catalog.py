from pathlib import Path
from bnsh.model_catalog import ModelCatalog

def test_catalog_is_readable():
    catalog = ModelCatalog(Path("models/catalog.json"))
    models = catalog.list()
    assert models
    assert all(model.id for model in models)
