from training.continuous_learning import LearningRun, SourceRecord

def test_learning_run_keeps_lineage():
    run = LearningRun(run_id="test-1", parent_model="ARIV-0.1")
    run.add_source(SourceRecord(
        source_id="source-1",
        locator="https://example.com",
        content_hash="abc123",
        retrieved_at="2026-01-01T00:00:00Z",
        usage_basis="test-only",
    ))
    run.datasets.append("dataset-v1")
    run.teachers.append("teacher-v1")
    run.mark_candidate("ariv-candidate-1")

    assert run.parent_model == "ARIV-0.1"
    assert run.sources[0].content_hash == "abc123"
    assert run.candidate_checkpoint == "ariv-candidate-1"
    assert run.status == "candidate"
