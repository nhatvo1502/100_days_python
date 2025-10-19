import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')
user_letter = int(input('How many letters would you like in your password?\n'))
user_symbol = int(input('How many symbols would you like?\n'))
user_number = int(input('How many numbers would you like?\n'))

#My solution
password = []

for l in range(user_letter):
    password+= random.choice(letters)

for n in range(user_number):
    password+= random.choice(numbers)

for s in range(user_symbol):
    password+= random.choice(symbols)

print(password)
random.shuffle(password)
print(password)
result = ''.join(password)
print(f"Your password is: {result}")