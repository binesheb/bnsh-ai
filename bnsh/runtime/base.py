from dataclasses import dataclass
from typing import Protocol, Iterator

@dataclass(frozen=True)
class ChatMessage:
    role: str
    content: str

@dataclass(frozen=True)
class GenerationConfig:
    temperature: float = 0.7
    max_tokens: int = 512
    top_p: float = 0.9

class InferenceProvider(Protocol):
    name: str
    def generate(self, messages: list[ChatMessage], config: GenerationConfig) -> str: ...
    def stream(self, messages: list[ChatMessage], config: GenerationConfig) -> Iterator[str]: ...

class RuntimeNotReady(RuntimeError):
    pass
