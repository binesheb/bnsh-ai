"""BNSH AI public Python package."""
__version__ = "0.2.0a1"

from .config import RuntimeConfig
from .messages import Message
from .model import ModelInfo
from .models import ModelManager, ModelRecord
from .runtime.facade import BNSHRuntime

__all__ = [
    "BNSHRuntime",
    "RuntimeConfig",
    "Message",
    "ModelInfo",
    "ModelManager",
    "ModelRecord",
    "__version__",
]
