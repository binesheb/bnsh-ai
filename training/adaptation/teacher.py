"""Teacher-model abstraction for ARIV adaptation workflows."""
from dataclasses import dataclass
from typing import Protocol

@dataclass(frozen=True)
class TeacherInfo:
    id: str
    revision: str
    usage_basis: str
    license: str | None = None

class Teacher(Protocol):
    @property
    def info(self) -> TeacherInfo: ...

    def generate(self, prompt: str, **kwargs: object) -> str:
        """Generate a teacher response for an adaptation example."""
        ...

class StaticTeacher:
    """Deterministic development teacher used to validate the pipeline.

    This is deliberately not an AI model. Production adapters will wrap
    compatible local or remote models.
    """
    def __init__(self, response: str = "development response") -> None:
        self._response = response
        self._info = TeacherInfo(
            id="static-development-teacher",
            revision="0",
            usage_basis="development-test-only",
        )

    @property
    def info(self) -> TeacherInfo:
        return self._info

    def generate(self, prompt: str, **kwargs: object) -> str:
        return self._response
