"""Optional Hugging Face Transformers backend.

Install the optional dependency group before using this backend:
    pip install -e ".[transformers]"
"""
from typing import Any

from ..model import ModelInfo
from .base import Backend

class TransformersBackend(Backend):
    """Run a causal language model through Transformers."""

    def __init__(self, model_id: str, device: str = "auto", **load_kwargs: Any) -> None:
        try:
            from transformers import AutoModelForCausalLM, AutoTokenizer
        except ImportError as exc:
            raise ImportError(
                'Transformers support is optional. Install with: '
                'pip install -e ".[transformers]"'
            ) from exc

        self.model_id = model_id
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map=device,
            **load_kwargs,
        )

    def chat(self, prompt: str, **kwargs: Any) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt")
        inputs = {k: v.to(self.model.device) for k, v in inputs.items()}
        output = self.model.generate(**inputs, **kwargs)
        generated = output[0][inputs["input_ids"].shape[-1]:]
        return self.tokenizer.decode(generated, skip_special_tokens=True)

    def info(self) -> ModelInfo:
        config = self.model.config
        parameter_count = config.num_parameters() if hasattr(config, "num_parameters") else None
        return ModelInfo(
            id=self.model_id,
            architecture=(config.architectures or [None])[0],
            parameter_count=parameter_count,
            context_length=getattr(config, "max_position_embeddings", None),
            modality="text",
        )
