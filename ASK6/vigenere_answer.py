def decryption(string, key):
    decrypt_text = []
    for i in range(len(string)):
        if string[i].isalpha():  # Check if the character is an alphabet letter
            decr_char = string[i]
            if decr_char.islower():
                decr_char = string[i].upper()
            x = (ord(decr_char) - ord(key[i % len(key)]) + 26) % 26
            x += ord('A')
            if string[i].islower():
                decrypt_text.append(chr(x).lower())  # Converting the resulting ASCII number to the corresponding character
            else:
                decrypt_text.append(chr(x))
        else:
            decrypt_text.append(string[i])  # Non-alphabet characters are not modified
    return "".join(decrypt_text)

if __name__ == "__main__":
    string = "DVID{l4cb3B_Abgm7s0qz4zg3b}"
    key = "secret"
    print("Decrypted message:", decryption(string, key))
