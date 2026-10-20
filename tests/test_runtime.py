import pytest

from bnsh import BNSHRuntime


def test_runtime_requires_backend():
    runtime = BNSHRuntime()
    with pytest.raises(RuntimeError, match="No ARIV model runtime is loaded"):
        runtime.chat("Hello")
