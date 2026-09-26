from bnsh import BNSHRuntime, ModelInfo
from bnsh.backends import EchoBackend

class InfoBackend(EchoBackend):
    def info(self):
        return ModelInfo(id="development", architecture="echo", languages=("en",))

def test_model_info():
    runtime = BNSHRuntime(backend=InfoBackend())
    assert runtime.model_info().id == "development"
