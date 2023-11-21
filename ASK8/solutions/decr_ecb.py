from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import binascii

# Ciphertext and AES-128 key
ciphertext_hex = "6314f025f4bc624cf9564f2fcc7864f0e6583a63bd989cb05638bcae146e0d1b663fafeaf1ebe24dc838701d35dd6a6d"
key_hex = "9473e715b15dd07f488c0b6e226ddce7"

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
