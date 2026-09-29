# Updating BNSH AI

## Manual update

1. Pull the latest main commit.
2. Recreate the virtual environment with the supported Python version from pyproject.toml.
3. Install the project and required optional extras for the feature being used.
4. Run the test suite before deployment.

## Dependency updates

Dependabot checks Python and GitHub Actions dependencies weekly. Review and merge updates only after CI passes.

## Release policy

Use Semantic Versioning. Runtime behavior changes require a release; dependency-only maintenance uses a patch release when it changes the supported runtime baseline.
