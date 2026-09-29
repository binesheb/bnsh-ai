from bnsh import BNSHRuntime, __version__

def test_public_runtime_imports():
    assert BNSHRuntime is not None
    assert __version__

def test_development_runtime_chat():
    runtime = BNSHRuntime(model="development")
    response = runtime.chat("hello")
    assert "hello" in response
