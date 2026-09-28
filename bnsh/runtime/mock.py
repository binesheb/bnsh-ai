class MockARIVProvider:
    name = "mock"
    def generate(self, messages, config):
        user = next((m.content for m in reversed(messages) if m.role == "user"), "")
        return "ARIV development runtime is connected. You asked: " + user
    def stream(self, messages, config):
        yield self.generate(messages, config)
