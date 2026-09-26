# BNSH Runtime

The runtime is the stable application-facing layer between applications and model inference backends.

Current contract:
- chat(prompt)
- health()

Planned contracts:
- streaming
- structured output
- embeddings
- vision
- tool calls
- model metadata
- cancellation
- batching

Applications should depend on BNSHRuntime rather than a specific inference engine.

EchoBackend exists only to validate the contract and CI. It is not an AI model.
