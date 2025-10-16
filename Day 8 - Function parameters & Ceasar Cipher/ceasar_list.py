import os
list_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(word, shift):
   alphabet_list = []
   if word.islower() == True:
      alphabet_list = list_lower
   else:
      alphabet_list = list_upper
   pos = alphabet_list.index(word)
   encrypted_pos = (pos + shift) % len(alphabet_list)

   return alphabet_list[encrypted_pos]

def decode(word, shift):
   alphabet_list = []
   if word.islower() == True:
      alphabet_list = list_lower
   else:
      alphabet_list = list_upper
   encrypted_pos = alphabet_list.index(word)
   decrypted_pos = (encrypted_pos - shift) % len(alphabet_list)
   
   return alphabet_list[decrypted_pos]
   

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