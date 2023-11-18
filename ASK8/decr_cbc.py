from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import binascii

def decrypt_message(ciphertext_hex, key_hex, iv_hex):
    # Convert hexadecimal values to bytes
    ciphertext = binascii.unhexlify(ciphertext_hex)
    key = binascii.unhexlify(key_hex)
    iv = binascii.unhexlify(iv_hex)

    # Create the decryptor
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()

    # Decrypt the ciphertext
    decrypted_padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove the padding to obtain the original message
    unpadder = padding.PKCS7(128).unpadder()
    original_message_bytes = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    # Convert bytes to a string using UTF-8 encoding
    original_message = original_message_bytes.decode("utf-8")

    return original_message

# Example usage:
ciphertext_hex = "0bf81ae8f75f85b05eb51661158df2daa5a5002391d1cdd1ddc74ec2cb4f0bbc74c70ffbabcdfa8156cc77dc8c3bc86e"
key_hex = "10d86c0c76d0b6a086edb8b1e51d5947"
iv_hex = "552b5a95481ea5524fd708c126e0b024"
decrypted_message = decrypt_message(ciphertext_hex, key_hex, iv_hex)
print("Decrypted Message:", decrypted_message)
