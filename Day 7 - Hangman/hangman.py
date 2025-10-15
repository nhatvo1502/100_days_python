import random
words_list = ['haiku', 'poem', 'plant','coffee','tea']

print('Welcome to hangman')
word = random.choice(words_list).lower()
word_to_guess = []
for c in range(len(word)):
    word_to_guess.append("_")

print(word_to_guess)
print(f"Word to guess: {''.join(word_to_guess)}")

lives = len(word)

while lives > 0 and ("_" in word_to_guess):
    user_guess = input('Guess a letter: ')
    if user_guess in word:
        for pos in range(len(word)):
            if word[pos] == user_guess:
                word_to_guess[pos] = user_guess
        print(f"Word to guess: {''.join(word_to_guess)}")
    else:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life")
        lives -=1
        #-->draw another line on hangman picture
    print(f'**********************{lives}/{len(word)} LIVES LEFT*********************')

if lives > 0:
    print ('You win!')
else:
    print('You lost!')