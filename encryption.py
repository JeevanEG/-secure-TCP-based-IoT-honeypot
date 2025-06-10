from cryptography.fernet import Fernet

# ⚠️ Use this same key in both client and server
key = b'nvZUmhH_0W2_xVpjxsbHrEFjXc8ByEkLnJ3fRimhrdk='
cipher = Fernet(key)

def encrypt(data: bytes) -> bytes:
    return cipher.encrypt(data)

def decrypt(data: bytes) -> bytes:
    return cipher.decrypt(data)