# PRIDE Checksum

Computes SHA-1 checksum for all the files in the specified directory or for the list of all files specified in a file and writes to a `checksum.txt` file.

## Installation

Install from PyPI:

```bash
pip install pride-checksum
```

## Usage

**Option 1: Compute checksums for all files in a directory**

```bash
pride_checksum --out_path /path/to/save/computed_checksum/ --files_dir /dir_path/where/files/are/located/
```

**Option 2: Compute checksums for files listed in a file**

```bash
pride_checksum --out_path /path/to/save/computed_checksum/ --files_list_path /path/to/file/containing/list_of_files.txt
```

### Sample `list_of_files.txt`:
```
/path/to/some/file1.xml
/path/to/some/file2.xml
/some/other/path/file3.tsv
```

## Requirements

Please make sure the list of files:
* Doesn't contain any duplicate file names.
* Doesn't contain any directories (only files are allowed)
* Doesn't contain any hidden files.

## Important Notes

* **File names can't have any spaces or any special chars other than underscore(_) and hyphen (-)**
* The name of the output file is always `checksum.txt` and if a file with same name already exists in the specified out_path, it will be overwritten.

## Development

### Running Tests

```bash
pip install -e ".[dev]"
pytest tests/
```

### Building Package

```bash
pip install build
python -m build
```

## Publishing to PyPI

This package is automatically published to PyPI when a new release is created on GitHub. The publishing workflow:

1. Create a new release on GitHub with a version tag (e.g., `v1.2.0`)
2. The GitHub Actions workflow automatically builds and publishes the package to PyPI
3. The package becomes available at https://pypi.org/project/pride-checksum/

The publishing process uses PyPI's trusted publishing feature for secure authentication. 