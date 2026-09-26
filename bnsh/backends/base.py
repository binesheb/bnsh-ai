"""Backend abstractions."""
from abc import ABC, abstractmethod
from typing import Any

class Backend(ABC):
    @abstractmethod
    def chat(self, prompt: str, **kwargs: Any) -> str:
        raise NotImplementedError

class EchoBackend(Backend):
    """Development backend used to validate the runtime contract."""
    def chat(self, prompt: str, **kwargs: Any) -> str:
        return prompt
