# PyPI Publishing Setup Instructions

This repository is configured to automatically publish to PyPI when a release is created. This uses PyPI's "Trusted Publishing" feature for secure, token-free publishing.

## Setup Steps (for repository maintainers)

### 1. Configure PyPI Trusted Publishing

1. Go to https://pypi.org/manage/account/publishing/
2. Add a new "pending publisher" with these details:
   - **PyPI Project Name**: `pride-checksum`
   - **Owner**: `PRIDE-Archive`
   - **Repository name**: `pride-checksum`
   - **Workflow name**: `publish.yml`
   - **Environment name**: `pypi`

### 2. Create a Release

To publish a new version:

1. Update the version in `pyproject.toml`
2. Commit and push the changes
3. Create a new release on GitHub:
   - Go to https://github.com/PRIDE-Archive/pride-checksum/releases
   - Click "Create a new release"
   - Choose or create a tag (e.g., `v1.2.0`)
   - Add release notes
   - Click "Publish release"

### 3. Automatic Publishing

The GitHub Actions workflow (`.github/workflows/publish.yml`) will automatically:

1. Trigger when a release is published
2. Build the package using `python -m build`
3. Validate the package with `twine check`
4. Publish to PyPI using trusted publishing
5. The package will be available at https://pypi.org/project/pride-checksum/

## Workflow Features

- **Secure**: Uses OpenID Connect for authentication (no API tokens needed)
- **Automated**: Publishes only on releases, not on every commit
- **Validated**: Checks package integrity before publishing
- **Environment Protection**: Uses GitHub environment for additional security

## Manual Publishing (fallback)

If needed, you can publish manually:

```bash
# Install dependencies
pip install build twine

# Build the package
python -m build

# Check the package
twine check dist/*

# Upload to PyPI (requires API token)
twine upload dist/*
```