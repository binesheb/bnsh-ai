"""Configuration objects for BNSH AI."""
from dataclasses import dataclass

@dataclass(frozen=True)
class RuntimeConfig:
    model: str | None = None
    backend: str = "auto"
    temperature: float = 0.7
    max_tokens: int = 512
    system_prompt: str | None = None
