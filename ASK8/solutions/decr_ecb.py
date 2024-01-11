from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import binascii

# Ciphertext and AES-128 key
ciphertext_hex = "3f2fb77efca07c2ccdfb8279eb9d1a2c67828f27249cebef046691a9a22216923e96beda6c10df72369ad71d2b345bae"
key_hex = "f051a262f8d25a52c2c6f15b1448a17a"

# Convert hexadecimal values to bytes
ciphertext = binascii.unhexlify(ciphertext_hex)
key = binascii.unhexlify(key_hex)

# Create a cipher object using the key and ECB mode
cipher = Cipher(algorithms.AES(key), modes.ECB())

#Create the decryptor object
decryptor = cipher.decryptor()

# Decrypt the ciphertext
decrypted_padded_data = decryptor.update(ciphertext) + decryptor.finalize()

# Remove the padding to obtain the original message
unpadder = padding.PKCS7(128).unpadder()
original_message_bytes = unpadder.update(decrypted_padded_data) + unpadder.finalize()

# Convert bytes to a string using UTF-8 encoding
original_message = original_message_bytes.decode("utf-8")

print("Decrypted Message:", original_message)
