from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import secrets

# Generate a random 128-bit (16-byte) key
key = secrets.token_bytes(16)

# Message to be encrypted and conversion to bytes using UTF-8 encoding
message = "Here is your second half : _Br3ak3r}"
message_bytes = message.encode('utf-8')

#Creates a padding object with a block size of 128 bits
padder = padding.PKCS7(128).padder()
#Applies the padding to the message to ensure it's a multiple of 16 bytes
padded_data = padder.update(message_bytes) + padder.finalize()


#Using the generated key we create a cipher object in ECB mode
cipher = Cipher(algorithms.AES(key), modes.ECB())  

# Creates an encryptor object using the cipher we created before 
encryptor = cipher.encryptor()

# Encrypts the padded message using the encryptor
ciphertext = encryptor.update(padded_data) + encryptor.finalize()


print("Encrypted Message:", ciphertext.hex())
print("AES-128 Key:", key.hex())
