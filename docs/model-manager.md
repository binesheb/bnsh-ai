# BNSH Model Manager

The model manager provides a stable local model lifecycle independent of the inference backend.

## Current commands

```bash
bnsh model list
bnsh model register demo --source local --revision v1
bnsh model info demo
bnsh model remove demo
```

Models are stored under:

```
~/.bnsh/models/
```

The current implementation manages registration and metadata only. It deliberately does not download arbitrary model weights yet.

## Next capabilities

- remote model catalogs
- resumable downloads
- SHA-256 verification
- model manifests
- cache management
- Hugging Face integration
- GGUF support
- signed release metadata
- disk-space checks
- safe extraction
- model compatibility checks

A model should only be considered installable after its source, license, architecture, files, and integrity can be identified.
