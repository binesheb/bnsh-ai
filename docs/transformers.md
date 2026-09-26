# Transformers Backend

BNSH provides an optional Hugging Face Transformers backend for local development and experimentation.

## Install

```bash
pip install -e ".[transformers]"
```

## Example

```python
from bnsh import BNSHRuntime
from bnsh.backends import TransformersBackend

backend = TransformersBackend("MODEL_ID")
runtime = BNSHRuntime(model="MODEL_ID", backend=backend)

print(runtime.chat("Hello"))
```

## Design notes

Transformers is an optional dependency. The core BNSH package remains lightweight.

Do not assume that an arbitrary model is compatible with this backend. Architecture, tokenizer, chat template, hardware requirements, model license, and model-specific generation behavior must be checked before deployment.

The first backend is intentionally simple. Production work will add batching, streaming, device-aware loading, quantization, structured generation, and model-specific chat-template handling.
