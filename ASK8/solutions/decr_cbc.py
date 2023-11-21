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
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
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
ciphertext_hex = "fb7f81da836150a61848b7b30c8394fcebddc706322b0287108136691c4c5be674cf59fad621e34b43277cd634395823"
key_hex = "94425e60d1fba20b51f0cf35c6e95da3"
iv_hex = "4ec9d568b90e6ecc1fbb34522974c381"
decrypted_message = decrypt_message(ciphertext_hex, key_hex, iv_hex)
print("Decrypted Message:", decrypted_message)
