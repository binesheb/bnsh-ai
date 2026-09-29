"""Runtime service for the local Control API."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from bnsh.runtime import ChatMessage, GenerationConfig, RuntimeManager, RuntimeNotReady
from bnsh.runtime.mock import MockARIVProvider


class RuntimeService:
    def __init__(self) -> None:
        self.runtime = RuntimeManager()
        self.runtime.load("development", MockARIVProvider())

    def status(self) -> dict:
        return {
            "state": "ready" if self.runtime.ready else "idle",
            "model_id": self.runtime.model_id,
            "backend": self.runtime.provider,
            "message": "Development runtime" if self.runtime.provider == "mock" else "",
        }

    def chat(self, message: str) -> dict:
        if not message.strip():
            return {"ok": False, "error": "invalid_request", "message": "Message is empty."}
        try:
            response = self.runtime.generate(
                [ChatMessage(role="user", content=message)],
                GenerationConfig(),
            )
            return {"ok": True, "response": response}
        except RuntimeNotReady as exc:
            return {"ok": False, "error": "runtime_not_ready", "message": str(exc)}
