"""Backend abstractions."""
from abc import ABC, abstractmethod
from typing import Any, Iterable
from ..messages import Message
from ..model import ModelInfo

class Backend(ABC):
    @abstractmethod
    def chat(self, prompt: str, **kwargs: Any) -> str:
        raise NotImplementedError

    def chat_messages(self, messages: Iterable[Message], **kwargs: Any) -> str:
        """Default adapter from messages to a single prompt."""
        parts = [f"{m.role}: {m.content}" for m in messages]
        return self.chat("\n".join(parts), **kwargs)

    def info(self) -> ModelInfo | None:
        return None

class EchoBackend(Backend):
    """Development backend used to validate the runtime contract."""
    def chat(self, prompt: str, **kwargs: Any) -> str:
        return prompt
