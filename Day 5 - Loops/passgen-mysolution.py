import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')
letter = int(input('How many letters would you like in your password?\n'))
symbol = int(input('How many symbols would you like?\n'))
number = int(input('How many numbers would you like?\n'))

#My solution
password = []

for l in range(letter - symbol - number):
    password.append(letters[random.randint(0, len(letters)-1)])

for n in range(number):
    password.append(numbers[random.randint(0, len(numbers)-1)])

for s in range(symbol):
    password.append(symbols[random.randint(0, len(symbols)-1)])

print(password)
random.shuffle(password)
print(password)
result = ''.join(password)
print(f"Your password is: {result}")