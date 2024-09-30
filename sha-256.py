import hashlib

def generate_sha256(file_path):
    """Generate SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    
    # Open file in binary mode
    with open(file_path, "rb") as file:
        # Read the file in chunks to avoid memory overload for large files
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)
    
    # Return the hexadecimal hash signature
    return sha256_hash.hexdigest()

def verify_sha256(file_path, expected_hash):
    """Verify the file's integrity by comparing its SHA-256 hash with the expected hash."""
    generated_hash = generate_sha256(file_path)
    
    if generated_hash == expected_hash:
        return True
    else:
        return False


file_to_hash = 'file.txt'

# Generate the hash of the file
file_hash = generate_sha256(file_to_hash)
print(f"Generated SHA-256 Hash: {file_hash}")

# For verification
is_valid = verify_sha256(file_to_hash, file_hash)  # You can replace file_hash with any expected hash for verification
if is_valid:
    print("File is valid, the hash matches.")
else:
    print("File verification failed, the hash does not match.")
