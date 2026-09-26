"""Core BNSH AI runtime interface."""
from dataclasses import dataclass
from typing import Any, Iterable

from .backends import Backend
from .config import RuntimeConfig
from .messages import Message
from .model import ModelInfo

@dataclass
class BNSHRuntime:
    """Stable application-facing entry point for BNSH inference."""
    model: str | None = None
    backend: Backend | None = None
    config: RuntimeConfig | None = None

    def __post_init__(self) -> None:
        if self.config is None:
            self.config = RuntimeConfig(model=self.model)
        if self.model is None:
            self.model = self.config.model

    def chat(self, prompt: str, **kwargs: Any) -> str:
        if not isinstance(prompt, str) or not prompt.strip():
            raise ValueError("prompt must be a non-empty string")
        if self.backend is None:
            raise RuntimeError("No inference backend is configured.")
        return self.backend.chat(prompt, **kwargs)

    def chat_messages(self, messages: Iterable[Message], **kwargs: Any) -> str:
        if self.backend is None:
            raise RuntimeError("No inference backend is configured.")
        return self.backend.chat_messages(messages, **kwargs)

    def model_info(self) -> ModelInfo | None:
        return self.backend.info() if self.backend is not None else None

    def health(self) -> dict[str, Any]:
        return {"status": "ok" if self.backend is not None else "unconfigured", "model": self.model}
