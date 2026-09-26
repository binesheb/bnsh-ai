"""Core runtime interface.

The initial runtime intentionally provides a stable abstraction without
coupling the project to a particular model or inference backend.
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class BNSHRuntime:
    """Entry point for BNSH model inference.

    A future backend can implement model loading, generation, streaming,
    embeddings, vision, and tool use behind this interface.
    """

    model: str | None = None
    backend: Any | None = None

    def chat(self, prompt: str, **kwargs: Any) -> str:
        """Generate a response using the configured backend."""
        if self.backend is None:
            raise RuntimeError(
                "No inference backend is configured yet. "
                "BNSH AI 0.1 is currently the runtime architecture phase."
            )

        return self.backend.chat(prompt, **kwargs)
