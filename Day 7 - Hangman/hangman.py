import random
words_list = ['haiku', 'poem', 'plant','coffee','tea']

print('Welcome to hangman')
word = random.choice(words_list)
display_word = ''
for c in range(len(word)):
    if c == (len(word)-1):
        display_word+='_'
    else:
        display_word+='_ '

lives = len(word)

while lives > 0:
    user_guess = input('Guess a letter: ')
    

print(word)
print(display_word)