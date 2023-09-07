#credits: https://www.codespeedy.com/vigenere-cipher-using-python/#google_vignette
  
def encryption(string, key):
    encrypt_text = []
    for i in range(len(string)):
        if string[i].isalpha():  # Check if the character is an alphabet letter
            encr_char = string[i]
            if(encr_char.islower()):
                encr_char = string[i].upper()
            x = (ord(encr_char) + ord(key[i % len(key)])) % 26 #Get Ascii values of characters and make sure they stay within the alphabetical range
            x += ord('A') #add the ascii value of A 
            if(string[i].islower()):
                encrypt_text.append(chr(x).lower()) #converting the resulting Ascii number to the corresponding character
              
            else:
                encrypt_text.append(chr(x))
        else:
            encrypt_text.append(string[i])  # Non-alphabet characters are not modified
    return "".join(encrypt_text)

  
if __name__ == "__main__": 
  string = "?" #this is the flag
  key = "?" #the key found from solving the caesar's encryption
  encrypt_text = encryption(string,key) 
  print("Encrypted message:", encrypt_text)
