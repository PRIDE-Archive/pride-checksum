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

## Usage

The tool provides two modes of operation:

### Mode 1: Process all files in a directory
```bash
pride_checksum --files_dir /path/to/your/files/ --out_path /path/to/save/checksum/
```

### Mode 2: Process files from a list
```bash
pride_checksum --files_list_path /path/to/files_list.txt --out_path /path/to/save/checksum/
```

### Command-line options
- `--files_dir`: Directory containing files to checksum (processes all files in the directory)
- `--files_list_path`: Path to a text file containing list of files to process
- `--out_path`: Directory where the `checksum.txt` file will be saved (**required**)

**Note**: You must specify either `--files_dir` OR `--files_list_path`, but not both.

## Examples

### Example 1: Processing a directory
```bash
# Create some test files
mkdir my_data
echo "Sample content" > my_data/file1.txt
echo "More data" > my_data/file2.xml

# Generate checksums
mkdir checksums
pride_checksum --files_dir my_data --out_path checksums

# View the results
cat checksums/checksum.txt
```

### Example 2: Processing files from a list
Create a file list (`my_files.txt`):
```
/home/user/documents/report.pdf
/home/user/data/experiment1.csv
/home/user/data/experiment2.csv
```

Then run:
```bash
pride_checksum --files_list_path my_files.txt --out_path /home/user/checksums/
```

### Example Output
The generated `checksum.txt` file contains tab-separated values with filename and SHA-1 hash:

```
# SHA-1 Checksum 
file1.txt	aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
file2.xml	356a192b7913b04c54574d18c28d46e6395428ab
report.pdf	da39a3ee5e6b4b0d3255bfef95601890afd80709
```

## File Requirements and Limitations

### Supported Files
- ✅ Regular files only (no directories)
- ✅ Any file type and size
- ✅ Files with alphanumeric names
- ✅ Files with underscores (`_`) and hyphens (`-`)

### Restrictions
- ❌ **No spaces in filenames** - files with spaces will be rejected
- ❌ **No special characters** except underscore and hyphen
- ❌ **No hidden files** (files starting with `.`)
- ❌ **No directories** in the file list
- ❌ **No duplicate filenames** (even if in different paths)

### Valid filename examples:
```
✅ data_file.txt
✅ experiment-01.csv
✅ report_2024.pdf
✅ analysis123.xml
```

### Invalid filename examples:
```
❌ file with spaces.txt
❌ file@symbol.txt
❌ .hidden_file
❌ data%file.csv
```

## Important Notes

⚠️ **Overwrite Behavior**: If `checksum.txt` already exists in the output directory, it will be **automatically overwritten** without confirmation.

📝 **Progress Tracking**: The tool displays progress as it processes files:
```
[ 1 / 3 ] Processing: /path/to/file1.txt
[ 1 / 3 ] Generated checksum for: file1.txt -> aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
[ 2 / 3 ] Processing: /path/to/file2.xml
...
```

🔍 **Validation**: The tool performs extensive validation:
- Checks if files exist and are accessible
- Validates filename format
- Detects duplicate filenames
- Ensures output directory exists and is writable

## Troubleshooting

### Common Issues

**Error: "Directory doesn't exist"**
- Ensure the `--files_dir` path exists and is accessible
- Check that `--out_path` directory exists (create it if needed)

**Error: "Invalid filename"**
- Rename files to use only alphanumeric characters, underscores, and hyphens
- Remove spaces and special characters from filenames

**Error: "Hidden files are not allowed"**
- Remove hidden files (starting with `.`) from your directory or file list

**Error: "Following files have duplicate entries"**
- Ensure all files have unique names, even if they're in different directories
- Rename duplicate files before processing

**Error: "No permissions to write"**
- Check write permissions on the output directory
- Ensure you have sufficient disk space

## Development

### Running Tests
```bash
python -m pytest tests/ -v
```

### Project Structure
```
pride-checksum/
├── src/pride_checksum/    # Main source code
├── tests/                 # Test files
├── README.md             # This file
└── pyproject.toml        # Project configuration
```

## Use Cases

- **Research Data Management**: Verify integrity of research datasets
- **Archive Validation**: Ensure archived files haven't been corrupted
- **Data Transfer Verification**: Confirm files transferred correctly
- **Backup Validation**: Verify backup integrity
- **Compliance Auditing**: Generate checksums for audit trails
- **Quality Assurance**: Validate data in automated pipelines 