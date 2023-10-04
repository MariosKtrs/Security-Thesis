#credits: https://www.scaler.com/topics/caesar-cipher-python/

#We need to decrypt the message between the curly brackets of the FLAG file
input_data="ykixkz"


upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_letters = 'abcdefghijklmnopqrstuvwxyz'

for key in range(52):
   translated = ''
   #For every character in the input data variable, we check if the character is lowercase
   #or uppercase. Then we find the character's numerical position in the upper_letters or
   #lower_letters variable and we subtract the key to perform the correct shift. Then, we
   #we add mod 26 to ensure that the shift stays within the alphabetical range.
   for ch in input_data:
       if (ch.isupper()):
            num = (upper_letters.find(ch) - key) % 26
            translated = translated + upper_letters[num]            
       else:
            num = (lower_letters.find(ch) - key) % 26
            translated = translated + lower_letters[num]
           
   print('Hacking key is %s: %s' % (key, translated))

