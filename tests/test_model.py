from bnsh import ModelInfo
from bnsh.backends import EchoBackend


class InfoBackend(EchoBackend):
    def info(self):
        return ModelInfo(id="development", architecture="echo", languages=("en",))


def test_backend_model_info():
    info = InfoBackend().info()
    assert info is not None
    assert info.id == "development"
    assert info.architecture == "echo"
    assert info.languages == ("en",)
