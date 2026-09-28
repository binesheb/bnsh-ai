# ARIV Data

The repository stores **metadata and schemas**, not large training corpora.

Every dataset used for ARIV development should have a dataset manifest containing:

- dataset identifier
- version
- source
- license or usage basis
- languages
- approximate size
- collection date where applicable
- preprocessing steps
- deduplication method
- PII handling
- known limitations

A future release may use Hugging Face Datasets, object storage, or another dedicated dataset distribution system.

Do not add a dataset to training merely because it is publicly accessible.
