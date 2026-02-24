import hashlib
import sys
import os

def calculate_file_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)

    return sha256.hexdigest()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("请拖入一个文件到终端运行")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print("文件不存在")
        sys.exit(1)

    file_hash = calculate_file_hash(file_path)

    print("\n文件:", file_path)
    print("SHA256:", file_hash)
