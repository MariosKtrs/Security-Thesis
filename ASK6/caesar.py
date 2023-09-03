#credits: https://www.scaler.com/topics/caesar-cipher-python/

#Function that takes the text and the shift number as arguments
def encryption(input,shift):
    

    #This is wear the encrypted text will be stored    
    encr_text="";

    # Iterate over each character of the text
    for char in input_data:
        # check if a character is uppercase then encrypt it accordingly 
        if (char.isupper()):
            encr_text += chr((ord(char) + shift-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly 
        elif (char.islower()):
            encr_text += chr((ord(char) + shift-97) % 26 + 97)
       
    return encr_text

#Opening input file and storing its contents into the input_data variable 
input = open("FLAG", "r")
input_data = input.read()
input.close()

shift = #? Create a script that bruteforces all possible shifts! 

print("Original Text is : " + input_data)
print("Shift pattern is : " + str(shift))
print("Cipher Text is : " + encryption(input_data,shift))
