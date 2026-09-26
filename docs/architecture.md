# BNSH AI Architecture

## Layers

### 1. Model layer

Contains model weights, tokenizer assets, configuration, and model metadata.

### 2. Inference layer

Provides backend adapters for supported runtimes such as local CPU/GPU inference and optimized serving engines.

### 3. BNSH Runtime

Provides a stable application-facing interface for:

- text generation
- chat
- streaming
- embeddings
- vision
- tool calling
- structured output

### 4. Service layer

Optional HTTP/API services expose the runtime to applications and devices.

### 5. BINESH OS integration

BINESH OS should consume BNSH through the stable runtime/service interface. It must not depend directly on internal model implementation details.

## Deployment targets

The architecture should support:

- CPU-only development
- consumer GPU systems
- dedicated GPU servers
- cloud inference
- quantized edge inference
- offline BINESH OS deployments

## Model/data separation

Source code, model weights, and datasets should have independent lifecycle and licensing documentation. Large weights and datasets should not be committed to the Git repository.
