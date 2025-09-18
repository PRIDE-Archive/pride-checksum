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
=======
# PRIDE Checksum Generator

A command-line tool that computes SHA-1 checksums for files and generates integrity verification reports. This tool is essential for data validation, file integrity checking, and ensuring data hasn't been corrupted during transfer or storage.

## Why do you need this tool?

**Data Integrity Verification**: When working with important files (research data, archives, backups), you need to ensure files haven't been corrupted, modified, or tampered with during:
- File transfers between systems
- Long-term storage
- Data migrations
- Backup and restore operations

**Compliance and Auditing**: Many organizations require checksum verification for:
- Data governance and compliance
- Scientific research reproducibility
- Archive validation
- Quality assurance processes

**Batch Processing**: Instead of manually computing checksums for individual files, this tool efficiently processes entire directories or file lists, making it ideal for:
- Large datasets
- Automated workflows
- Data pipelines
- Archive management

## Installation

### Prerequisites
- Python 3.11 or higher
- pip package manager

### Install from source
```bash
git clone https://github.com/PRIDE-Archive/pride-checksum.git
cd pride-checksum
pip install -e .
```

### Install for development
```bash
pip install -e ".[dev]"
```

