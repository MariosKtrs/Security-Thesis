from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import secrets

# Generate a random 128-bit (16-byte) key
key = secrets.token_bytes(16)

# Message to be encrypted and conversion to bytes using UTF-8 encoding
message = "Here is your second half : _Br3ak3r}"
message_bytes = message.encode('utf-8')

# Ensure the message is a multiple of 16 bytes (AES block size) using PKCS7 padding
padder = padding.PKCS7(128).padder()
padded_data = padder.update(message_bytes) + padder.finalize()


#Using ECB mode for encryption
cipher = Cipher(algorithms.AES(key), modes.ECB())  # Using ECB mode, change this as needed

# Create the encryptor
encryptor = cipher.encryptor()

# Encrypt the message
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

# The 'ciphertext' contains the encrypted message
print("Encrypted Message:", ciphertext.hex())

# The generated 128-bit key
print("AES-128 Key:", key.hex())
