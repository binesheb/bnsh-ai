"""Development provider kept for installation and API smoke tests."""
from .base import ChatMessage, GenerationConfig


class MockARIVProvider:
    name = "mock"

    def generate(self, messages: list[ChatMessage], config: GenerationConfig) -> str:
        user = next((m.content for m in reversed(messages) if m.role == "user"), "")
        return "ARIV development runtime is connected. You asked: " + user

    def stream(self, messages: list[ChatMessage], config: GenerationConfig):
        yield self.generate(messages, config)
