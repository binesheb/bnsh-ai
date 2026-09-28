from .base import ChatMessage, GenerationConfig, InferenceProvider, RuntimeNotReady

class RuntimeManager:
    def __init__(self):
        self._provider = None
        self.model_id = None
    @property
    def ready(self): return self._provider is not None
    @property
    def provider(self): return self._provider.name if self._provider else None
    def load(self, model_id: str, provider: InferenceProvider):
        self.model_id, self._provider = model_id, provider
    def generate(self, messages, config):
        if not self._provider: raise RuntimeNotReady("No ARIV model runtime is loaded.")
        return self._provider.generate(messages, config)
