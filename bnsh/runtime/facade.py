"""Simple public BNSHRuntime facade."""
from __future__ import annotations

from .base import ChatMessage, GenerationConfig, RuntimeNotReady
from .manager import RuntimeManager
from .mock import MockARIVProvider


class BNSHRuntime:
    def __init__(self, model: str | None = None, backend: str = "auto"):
        self.model = model
        self.backend = backend
        self.manager = RuntimeManager()
        if backend == "mock" or model == "development":
            self.manager.load(model or "development", MockARIVProvider())

    def chat(self, message: str) -> str:
        if not message.strip():
            raise ValueError("message must not be empty")
        return self.manager.generate(
            [ChatMessage(role="user", content=message)],
            GenerationConfig(),
        )
