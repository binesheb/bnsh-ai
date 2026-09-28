"""Runtime service used by the local Control API.

The first implementation is intentionally explicit: no model is silently
downloaded or loaded. A real backend is attached only after a published
ARIV artifact and compatible inference engine are available.
"""
from bnsh.runtime import Runtime


class RuntimeService:
    def __init__(self) -> None:
        self.runtime = Runtime()

    def status(self) -> dict:
        s = self.runtime.status
        return {
            "state": s.state,
            "model_id": s.model_id,
            "backend": s.backend,
            "message": s.message,
        }

    def chat(self, message: str) -> dict:
        try:
            response = self.runtime.generate(message)
            return {"ok": True, "response": response}
        except RuntimeError as exc:
            return {
                "ok": False,
                "error": "runtime_not_ready",
                "message": str(exc),
            }
        except ValueError as exc:
            return {"ok": False, "error": "invalid_request", "message": str(exc)}
