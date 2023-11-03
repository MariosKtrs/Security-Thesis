import hashlib

#This function will compare the hash of every possible character set up to the maximum length with the hash of the word we are looking for
def break_hash(hashed_word, characters, min_length, max_length):
    for word_length in range(min_length, max_length+1):
        original_word = brute_force(hashed_word, characters, word_length) #This calls the function that brute forces all of the different character combination
        if original_word:
            return original_word
    return 0

def brute_force(hashed_word, characters, word_length):
    for word in generate_words(characters, word_length):
        print("Testing word :",word)  # Print the word being tested
        if create_hash(word) == hashed_word:
            return word
    return 0;

def generate_words(characters, length): #This function returns a list of all possible character combinations for a given length
    candidates = [""]  #This array is the one that will contain the finished words
    for i in range(length): #We need to create words of the aproppriate length
        new_candidates = [] #This is a temporary list that will help gradually build all of the word combinations
        for char in characters: #Iterating through every character to build all different combinations
            for candidate in candidates: #Since the candidates list is never deleted, we iterate through every incomplete word of this list and append the given word plus the next character to the new_candidates list. 
                new_candidates.append(candidate + char)  
        candidates = new_candidates #this will replace the old list with the new one that contains everything the old list had plus a new character for each word
    return candidates

def create_hash(plaintext):
    return hashlib.sha256(plaintext.encode()).hexdigest()

if __name__ == "__main__":
    hashed_word = "2d483a5c34b6ce560784ca077a1840f67bced664501af472734bd9ebac87d44b"
    characters = "abcdefghijklmnopqrstuvwxyz"
    min_length = 1
    max_length = 5
    original_word = break_hash(hashed_word, characters, min_length, max_length)
    print("Original word is :",original_word)
