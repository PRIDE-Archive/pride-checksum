Computes SHA-1 checksum for all the files in the specified directory and writes to checksum.txt file.

**Usage:**

pride_checksum --files_dir /dir_path/where/files/are/located/

OR

pride_checksum --files_list_path /path/to/file/containing/list_of_file.txt

Sample `list_of_file.txt`
```
/path/to/some/file1.xml
/path/to/some/file2.xml
/some/other/path/file3.tsv
```
Please make sure the list of files:
* Doesn't contain any duplicate file names.
* Doesn't contain any directories (only files are allowed)
* Doesn't contain any hidden files.

**NOTE:**
* **File names can't have any spaces or any special chars other than underscore(_) and hyphen (-)**

* The path to the computed `checksum.txt` file will be printed at the end of the log. If `checksum.txt` already exists, it will be overwritten. 