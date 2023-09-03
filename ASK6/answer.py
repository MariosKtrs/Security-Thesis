#credits: https://www.scaler.com/topics/caesar-cipher-python/

#We need to decrypt the message between the curly brackets of the FLAG file
input_data="TrvjriTzgyvi"


upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_letters = 'abcdefghijklmnopqrstuvwxyz'

for key in range(52):
   translated = ''
   for ch in input_data:
       if (ch.isupper()):
            num = upper_letters.find(ch) - key
            if num < 0:
                num = num + len(upper_letters)
                translated = translated + upper_letters[num]
            else:
                translated = translated + ch
       else:
            num = lower_letters.find(ch) - key
            if num < 0:
                num = num + len(lower_letters)
                translated = translated + lower_letters[num]
            else:
                translated = translated + ch
   print('Hacking key is %s: %s' % (key, translated))

