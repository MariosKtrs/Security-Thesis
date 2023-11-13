from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import binascii

# Ciphertext and AES-128 key
ciphertext_hex = "a1b2abac8a5e380ded7fae14d7a3f202fd6364e37dc8320399f16141bcfdc9b751ced1471fb31b38051462d201cd0d4c"
key_hex = "9d9072260d78eb9fd3f950a2cbf0dada"

# Convert hexadecimal values to bytes
ciphertext = binascii.unhexlify(ciphertext_hex)
key = binascii.unhexlify(key_hex)

# Create the decryptor
backend = default_backend()
cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
decryptor = cipher.decryptor()

# Decrypt the ciphertext
decrypted_padded_data = decryptor.update(ciphertext) + decryptor.finalize()

# Remove the padding to obtain the original message
unpadder = padding.PKCS7(128).unpadder()
original_message_bytes = unpadder.update(decrypted_padded_data) + unpadder.finalize()

# Convert bytes to a string using UTF-8 encoding
original_message = original_message_bytes.decode("utf-8")

print("Decrypted Message:", original_message)
