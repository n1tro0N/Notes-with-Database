import hashlib

def hash_password(password: str):
    password_bytes = password.encode('utf-8')
    hashed_bytes = hashlib.sha256(password_bytes)
    hashed_password = hashed_bytes.hexdigest()
    return hashed_password