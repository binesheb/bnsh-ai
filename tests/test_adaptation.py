from pathlib import Path

from training.adaptation.generate import generate_dataset
from training.adaptation.teacher import StaticTeacher

def test_teacher_dataset_generation(tmp_path: Path):
    output = tmp_path / "adaptation.jsonl"
    count = generate_dataset(
        ["Hello", "Explain ARIV"],
        StaticTeacher("test response"),
        output,
    )
    assert count == 2
    lines = output.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 2
    assert '"teacher"' in lines[0]
