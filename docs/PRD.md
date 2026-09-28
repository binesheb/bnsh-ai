# BNSH AI / ARIV — Product Requirements Document

**Status:** Pre-alpha  
**Document:** Canonical product requirements  
**Last updated:** 2026-09-28

## 1. Product definition

**BNSH AI** is the open AI ecosystem.

**ARIV** is the foundation-model family created by BNSH AI.

**BNSH Runtime** is the software layer that runs ARIV and supported external models.

**BNSH SDK/API** provides developer integration.

**BINESH OS** is a major operating-system and edge deployment target.

The central product goal is to build an independently developed, openly accessible, multilingual AI model family that people can download, run, integrate, fine-tune, evaluate, and build products with according to each release's license.

## 2. Product vision

Build an AI platform that can:

- run locally on ordinary computers where model size permits
- scale to GPU servers and cloud infrastructure
- support multilingual and Indian-language intelligence
- learn from approved existing models through teacher/adaptation workflows
- acquire fresh information through a controlled web research system
- maintain a continuously updated knowledge layer
- conduct reproducible training experiments
- evaluate whether new model generations actually improve
- provide stable APIs and SDKs for developers
- serve as the intelligence layer for BINESH OS
- remain independently identifiable as ARIV rather than a rebranded external model

## 3. Naming and identity

### Ecosystem

**BNSH AI**

### Model family

**ARIV**

Planned variants:

- ARIV — general foundation model
- ARIV-Instruct — instruction following/chat
- ARIV-Reason — reasoning
- ARIV-Coder — coding
- ARIV-Vision — vision-language

Possible size variants:

- ARIV-1B
- ARIV-3B
- ARIV-7B
- larger variants when justified by training results and available compute

External models such as Qwen, DeepSeek, Llama, Gemma, or other models may be supported by BNSH Runtime, but they must retain their original identity and licensing.

## 4. Target users

### Developers

Need:

- simple installation
- Python SDK
- CLI
- REST/API access
- local inference
- model downloads
- model metadata
- fine-tuning/adaptation tools

### Researchers

Need:

- reproducible datasets
- training configurations
- checkpoints
- evaluation tooling
- experiment lineage
- teacher-model integrations
- transparent model documentation

### Businesses

Need:

- private/local deployment
- API integration
- predictable model versions
- domain adaptation
- enterprise deployment options
- data isolation

### End users

Need:

- easy installation
- local AI where hardware permits
- multilingual interaction
- privacy-conscious operation
- accessible model variants

### BINESH OS

Needs:

- native BNSH Runtime integration
- local ARIV inference
- model management
- agent/tool interfaces
- offline/edge operation
- stable APIs across ARIV releases

## 5. Core architecture

```
                         BNSH AI
                            |
             +--------------+--------------+
             |                             |
          ARIV Models               BNSH Ecosystem
             |                             |
     +-------+-------+          +----------+----------+
     |       |       |          |          |          |
   Base   Instruct Reason    Runtime    Training  Evaluation
     |       |       |          |          |          |
     +-------+-------+----------+----------+----------+
                            |
                       BNSH SDK/API
                            |
             +--------------+--------------+
             |              |              |
          Windows          Linux         BINESH OS
```

## 6. Bootstrap and deployment

A new machine should be able to install the BNSH ecosystem with minimal manual setup.

Linux/macOS:

```bash
curl -fsSL https://raw.githubusercontent.com/binesheb/bnsh-ai/main/bootstrap.sh | bash
```

Windows:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\bootstrap.ps1
```

Bootstrap requirements:

- detect prerequisites
- create isolated environment
- install BNSH Runtime
- validate installation
- run tests
- avoid silently downloading large model weights
- remain safe to rerun
- support future hardware-specific profiles

Future profiles:

```
bnsh bootstrap --cpu
bnsh bootstrap --nvidia
bnsh bootstrap --amd
bnsh bootstrap --edge
bnsh bootstrap --server
```

## 7. Model management

Required CLI concepts:

```bash
bnsh model list
bnsh model install <model>
bnsh model info <model>
bnsh model verify <model>
bnsh model remove <model>
bnsh model run <model>
```

Model manager requirements:

- local model registry
- metadata
- revisions
- manifests
- checksums
- disk-space checks
- resumable downloads
- safe extraction
- compatibility validation
- model cache
- future remote model catalog

## 8. ARIV training pipeline

```
Data sources
    ↓
Provenance / usage checks
    ↓
Cleaning
    ↓
Deduplication
    ↓
Quality filtering
    ↓
Tokenizer
    ↓
Training dataset
    ↓
Pretraining / adaptation
    ↓
Checkpoint
    ↓
Evaluation
    ↓
Release candidate
```

The first objective is a small end-to-end experiment that validates the complete pipeline before large-scale compute is committed.

Training must support:

- reproducible configurations
- deterministic seeds where practical
- checkpointing
- resume
- experiment metadata
- dataset versioning
- model lineage
- evaluation artifacts

## 9. Data governance

Every training dataset should have a manifest containing:

- dataset identifier
- version
- source
- license/usage basis
- languages
- size
- collection date where applicable
- preprocessing
- deduplication
- PII handling
- known limitations

The project must not treat public accessibility as automatic permission to train on a dataset.

## 10. Learning from existing models

ARIV must be able to learn from compatible existing models without becoming a rebrand of those models.

Supported mechanisms:

### Teacher-generated data

```
Prompt set
   ↓
Teacher model
   ↓
Generated examples
   ↓
Filtering / verification
   ↓
ARIV training
```

### Distillation

Where technically and legally permitted, compatible teachers may provide richer signals such as logits.

### Parameter-efficient adaptation

LoRA/PEFT and similar approaches may be used for controlled experiments.

### Teacher pool

The architecture should eventually allow multiple approved teachers:

```
Qwen ──────┐
DeepSeek ──┤
Llama ─────┤
Gemma ─────┤
Other ─────┘
     ↓
 Teacher Pool
     ↓
 Candidate Knowledge/Data
     ↓
 ARIV
```

Teacher metadata must record model identity, revision, license/usage basis, access method, and provenance.

External model outputs must not automatically be treated as ground truth.

## 11. Continuous learning

ARIV should support controlled continuous learning.

### Primary loop

```
Internet / approved sources
          ↓
       Discovery
          ↓
 Collection + provenance
          ↓
 Policy / usage checks
          ↓
 Extraction / normalization
          ↓
 Deduplication / quality
          ↓
      Knowledge Store
       /            \
      /              \
 Retrieval          Training Queue
     |                  |
     |             Teacher models
     |                  |
     |             Candidate dataset
     |                  |
     |              Training
     |                  |
     |              Evaluation
     |                  |
     |           Candidate checkpoint
     |                  |
     +------------ Promotion gate
                        |
                    ARIV vNext
```

### Fast learning

Fresh information should normally enter a versioned retrieval/knowledge layer first.

This allows ARIV to answer with current information without constantly changing model weights.

### Deep learning

Information that demonstrates durable value can enter a candidate training pipeline and potentially contribute to a future ARIV checkpoint.

## 12. Autonomous research capability

ARIV may eventually operate an autonomous research loop that:

- discovers new information
- identifies changes
- collects permitted sources
- records provenance
- builds candidate datasets
- asks approved teacher models for examples
- runs experiments
- evaluates candidates
- compares against previous checkpoints
- produces release candidates

The system must not silently replace the production model.

### Autonomy levels

| Level | Capability | Production model changes |
|---|---|---|
| 0 | Manual research/training | Manual |
| 1 | Automated discovery | Manual |
| 2 | Automated dataset construction | Manual |
| 3 | Automated training experiments | Manual |
| 4 | Automated evaluation/candidate generation | Manual approval |
| 5 | Policy-controlled promotion | Explicitly configured |

Default deployment: **Level 2 or below.**

Higher autonomy requires explicit configuration, logging, rollback, provenance, and evaluation policies.

## 13. Internet learning safety

The internet is an untrusted input.

Fetched material must be treated as data, never as executable instructions.

The system must defend against:

- prompt injection
- poisoned training data
- malicious instructions
- fabricated information
- duplicated content
- unexpected personal information
- malware and dangerous files
- low-quality synthetic content

Every acquired item should retain:

- source identifier/URL
- retrieval timestamp
- content hash
- extraction method
- usage basis
- transformation history
- dataset/checkpoint lineage

## 14. Evaluation system

Every ARIV candidate should be evaluated against the current release.

Evaluation areas:

- multilingual quality
- Indian-language quality
- factuality
- instruction following
- reasoning
- coding
- tool use
- safety
- latency
- memory/resource requirements
- regression tests
- contamination/leakage where applicable

A model should not be promoted merely because it improves one benchmark.

## 15. Model lineage

Every checkpoint should be reproducible through machine-readable lineage:

```
ARIV-vNext
 ├── parent checkpoint
 ├── dataset versions
 ├── teacher models
 ├── training configuration
 ├── evaluation results
 └── software revision
```

## 16. API and SDK

Core experience:

```python
from bnsh import BNSHRuntime

ai = BNSHRuntime(model="ARIV")
response = ai.chat("Hello")
```

Future interfaces:

- Python SDK
- JavaScript/TypeScript SDK
- REST API
- OpenAI-compatible API where appropriate
- streaming
- embeddings
- tool calling
- structured output
- multimodal input/output

## 17. BINESH OS integration

BINESH OS should consume BNSH Runtime through stable interfaces.

Planned capabilities:

- local ARIV inference
- offline knowledge
- local model management
- agents
- system tools
- vision/audio capabilities
- edge AI
- private data processing

ARIV remains independent of BINESH OS and must be usable on other platforms.

## 18. Release strategy

### Phase 0 — Foundation

- repository
- runtime
- CLI
- bootstrap
- model manager
- dataset schemas
- training configuration
- evaluation framework

### Phase 1 — ARIV experiment

- tokenizer
- small model architecture
- tiny validated dataset
- first training run
- checkpoint format
- baseline evaluation

### Phase 2 — ARIV-1B/experimental scale

- larger curated multilingual dataset
- improved tokenizer
- distributed training
- teacher learning
- instruction tuning
- stronger evaluation

### Phase 3 — Public ARIV release

- documented checkpoint
- model card
- license
- checksums
- inference formats
- Hugging Face/model registry distribution
- SDK/API integration

### Phase 4 — Continuous learning

- web research
- knowledge store
- teacher pool
- automated dataset generation
- scheduled experiments
- candidate evaluation
- model lineage
- controlled promotion

### Phase 5 — BINESH OS integration

- native runtime
- local ARIV
- agents
- tools
- multimodal capabilities
- edge deployment

## 19. Non-goals

BNSH AI must not:

- simply rebrand an existing model as ARIV
- automatically ingest arbitrary internet content into model weights
- bypass model or dataset licenses
- silently modify production model weights
- claim capabilities without evaluation
- treat synthetic teacher output as automatically correct
- make the base installer download huge model weights without explicit user intent

## 20. Success criteria

The project succeeds when a developer can:

1. bootstrap BNSH on a supported machine
2. install an ARIV model
3. run ARIV locally
4. use ARIV through an SDK/API
5. inspect model provenance and version
6. adapt ARIV using approved data/teachers
7. reproduce a documented training experiment
8. evaluate a new checkpoint against a previous checkpoint
9. retrieve current knowledge without necessarily retraining the model
10. deploy ARIV as an intelligence layer inside BINESH OS

## 21. Long-term vision

BNSH AI should become an open AI ecosystem in which **ARIV is a continuously improving model family**, supported by reproducible training, evaluation, knowledge acquisition, model adaptation, developer tooling, and deployment infrastructure.

The defining architecture is:

```
                    BNSH AI
                       |
                      ARIV
                       |
       +---------------+---------------+
       |               |               |
    Training       Knowledge       Teacher Pool
       |               |               |
       +---------------+---------------+
                       |
              Evaluation / Lineage
                       |
                  ARIV vNext
                       |
             +---------+---------+
             |                   |
        BNSH Runtime        BINESH OS
             |
      Windows / Linux / Cloud / Edge
```

## 22. Public ARIV Model Distribution

ARIV models must be installable by ordinary users as well as developers.

### Installation paths

**Control Center**

```
Discover → Select ARIV → Hardware check → Install → Run
```

**CLI**

```bash
bnsh model list
bnsh model info ariv-3b
bnsh model install ariv-3b
bnsh model run ariv-3b
```

**Container**

A future official container image should allow server deployment without requiring the desktop Control Center.

**Model hubs**

Official ARIV releases may be distributed through BNSH Model Hub and compatible public model registries.

### Model catalog requirements

Each published model needs:

- stable model ID
- human-readable name
- family and variant
- release status
- model card
- supported platforms
- parameter count
- context length
- quantization variants where available
- artifact URLs
- file sizes
- SHA-256 checksums
- license
- release version
- hardware requirements
- supported inference backends

### Installation requirements

The installer must:

- detect hardware
- estimate storage requirements
- show the user what will be downloaded
- support resumable downloads
- verify checksums
- validate model metadata
- avoid silent large downloads
- provide progress
- support cancellation
- support uninstall
- support model updates
- maintain installed-model state

The model format must remain portable. Users must not be forced to use the BNSH GUI to run ARIV.

