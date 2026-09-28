"""Control-plane primitives for ARIV continuous learning.

This module intentionally provides orchestration metadata only. Network crawling,
model training, and production promotion remain separate components.
"""
from dataclasses import dataclass, field
from datetime import datetime, timezone

@dataclass(frozen=True)
class SourceRecord:
    source_id: str
    locator: str
    content_hash: str
    retrieved_at: str
    usage_basis: str

@dataclass
class LearningRun:
    run_id: str
    parent_model: str
    sources: list[SourceRecord] = field(default_factory=list)
    datasets: list[str] = field(default_factory=list)
    teachers: list[str] = field(default_factory=list)
    candidate_checkpoint: str | None = None
    status: str = "created"

    def add_source(self, source: SourceRecord) -> None:
        self.sources.append(source)

    def mark_candidate(self, checkpoint: str) -> None:
        self.candidate_checkpoint = checkpoint
        self.status = "candidate"

    def timestamp(self) -> str:
        return datetime.now(timezone.utc).isoformat()
