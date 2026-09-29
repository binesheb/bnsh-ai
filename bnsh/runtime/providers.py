"""Built-in inference providers.

The mock provider is always available for installation validation.
Optional real providers are loaded only when their dependencies are installed.
"""
from __future__ import annotations

from .base import ChatMessage, GenerationConfig


class MockProvider:
    name = "mock"

    def generate(self, messages: list[ChatMessage], config: GenerationConfig) -> str:
        user = next((m.content for m in reversed(messages) if m.role == "user"), "")
        return f"ARIV development runtime is connected. You asked: {user}"

    def stream(self, messages: list[ChatMessage], config: GenerationConfig):
        yield self.generate(messages, config)


def available_providers() -> list[str]:
    return ["mock"]
