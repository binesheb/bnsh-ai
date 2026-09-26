import pytest

from bnsh import BNSHRuntime


def test_runtime_requires_backend():
    runtime = BNSHRuntime(model="development")
    with pytest.raises(RuntimeError):
        runtime.chat("Hello")
