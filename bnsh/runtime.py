"""Model-agnostic BNSH inference runtime.

ARIV is the model family; this layer deliberately separates model files
from the inference engine so llama.cpp, Transformers, vLLM, or future
BNSH-native backends can be plugged in without changing the UI/API.
"""
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


@dataclass(frozen=True)
class RuntimeStatus:
    state: str
    model_id: str | None = None
    backend: str | None = None
    message: str = ""


class Backend(Protocol):
    name: str

    def load(self, model_path: Path) -> None: ...
    def generate(self, prompt: str, **kwargs) -> str: ...
    def unload(self) -> None: ...


class Runtime:
    def __init__(self) -> None:
        self._backend: Backend | None = None
        self._model_id: str | None = None

    @property
    def status(self) -> RuntimeStatus:
        if self._backend is None:
            return RuntimeStatus("idle", message="No inference backend loaded")
        return RuntimeStatus("ready", self._model_id, self._backend.name)

    def attach(self, model_id: str, backend: Backend, model_path: Path) -> RuntimeStatus:
        backend.load(model_path)
        self._backend = backend
        self._model_id = model_id
        return self.status

    def generate(self, prompt: str, **kwargs) -> str:
        if self._backend is None:
            raise RuntimeError("No model backend is loaded")
        if not prompt.strip():
            raise ValueError("Prompt cannot be empty")
        return self._backend.generate(prompt, **kwargs)

    def unload(self) -> RuntimeStatus:
        if self._backend:
            self._backend.unload()
        self._backend = None
        self._model_id = None
        return self.status
