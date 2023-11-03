import hashlib

def create_hash(plaintext):
    return hashlib.sha256(plaintext.encode()).hexdigest()

if __name__ == "__main__":
    word = "fdrsh"
    hashed_word = create_hash(word)
    print("Known Hash:", hashed_word)

