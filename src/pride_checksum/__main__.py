import hashlib
import os
import sys


def sha1sum(filename):
    with open(filename, 'rb', buffering=0) as f:
        return hashlib.file_digest(f, 'sha1').hexdigest()


def main():
    files_path = sys.argv[1]
    if not os.path.isdir(files_path):
        print("Directory doesn't exists: " + files_path)
        sys.exit(1)

    checksum_file = os.path.join(files_path, "checksum.txt")
    if os.path.isfile(checksum_file):
        print("checksum.txt already exists in path:", files_path)
        yes_no = input("Do you want to overwrite checksum.txt? [y/n]:")
        if str(yes_no).upper() != 'Y':
            print("Exiting...")
            sys.exit(0)
        else:
            cfile = open(checksum_file, 'w')
            cfile.write('')
            cfile.close()

    for filename in os.listdir(files_path):
        if filename == 'checksum.txt':
            continue
        f = os.path.join(files_path, filename)
        if os.path.isfile(f):
            sha1_sum = sha1sum(f)
            cfile = open(checksum_file, 'a')
            cfile.write(sha1_sum + '\t' + filename + '\n')
            cfile.close()


if __name__ == '__main__':
    main()

