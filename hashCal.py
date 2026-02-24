import hashlib

def calculate_file_hash(filepath):
    sha256 = hashlib.sha256()
    
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    
    return sha256.hexdigest()


if __name__ == "__main__":
    file_path = "your path file"
    file_hash = calculate_file_hash(file_path)
    print("SHA256:", file_hash)

