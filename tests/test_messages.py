import pytest
from bnsh.messages import Message

def test_message():
    assert Message("user", "hello").role == "user"

def test_empty_message_rejected():
    with pytest.raises(ValueError):
        Message("user", "")
