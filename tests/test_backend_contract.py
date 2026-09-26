from bnsh.backends import EchoBackend
from bnsh.messages import Message

def test_message_adapter():
    backend = EchoBackend()
    result = backend.chat_messages([
        Message("system", "You are helpful."),
        Message("user", "Hello"),
    ])
    assert "system: You are helpful." in result
    assert "user: Hello" in result

def test_echo_info_is_optional():
    assert EchoBackend().info() is None
