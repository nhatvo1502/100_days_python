import os
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'


def encode(word, shift):
   alphabet_string = ''
   if word.islower() == True:
      alphabet_string = alphabet_lower
   else:
      alphabet_string = alphabet_upper
   pos = alphabet_string.find(word)
   encrypted_pos = (pos + shift) % len(alphabet_string)

   return alphabet_string[encrypted_pos]

def decode(word, shift):
   alphabet_string = ''
   if word.islower() == True:
      alphabet_string = alphabet_lower
   else:
      alphabet_string = alphabet_upper
   encrypted_pos = alphabet_string.find(word)
   decrypted_pos = (encrypted_pos - shift) % len(alphabet_string)
   
   return alphabet_string[decrypted_pos]
   

print("Welcome to Ceasar Cipher")
retry = True
while retry:
   choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
   if choice == 'encode':
      message = input('Type your message: \n')
      shift_number = int(input('Type your shift number: \n'))
      encoded_message = ''
      for i in message:
         if i != ' ':
            print(f'letter= {i}, encoded= {encode(i, shift_number)}')
            encoded_message += encode(i, shift_number)
         else:
            encoded_message += i
      print(f'Here is your encoded result: {encoded_message}')
   
   elif choice == 'decode':
      message = input('Type your message: \n')
      shift_number = int(input('Type your shift number: \n'))
      decoded_message = ''
      for i in message:
         if i != ' ':
            print(f'letter= {i}, decoded= {decode(i, shift_number)}')
            decoded_message += decode(i, shift_number)
         else:
            decoded_message += ' '
      print(f'Here is your decode result: {decoded_message}')
   
   isRetry = input("Type 'yes' if you want to go again. Otherwise type 'no'")
   if isRetry != 'yes':
      retry = False