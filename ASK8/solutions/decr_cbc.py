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
ciphertext_hex = "1f91fedf338935ff8ec6fac6e588cfb0f9716ad55917db4837a24c287aa66a54eeadcc3edccbb694b8a65cf82675da67"
key_hex = "dccedbea415a20650b2d0c564deced4a"
iv_hex = "8281180d57a74dfced70c35d98dce93a"
decrypted_message = decrypt_message(ciphertext_hex, key_hex, iv_hex)
print("Decrypted Message:", decrypted_message)
