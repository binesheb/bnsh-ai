"""Message primitives shared by BNSH runtimes and adapters."""
from dataclasses import dataclass
from typing import Literal

Role = Literal["system", "user", "assistant", "tool"]

@dataclass(frozen=True)
class Message:
    role: Role
    content: str

    def __post_init__(self) -> None:
        if not self.content:
            raise ValueError("message content must not be empty")
