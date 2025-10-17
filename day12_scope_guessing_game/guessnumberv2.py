import random
guess_a_number = r'''
  ________                                                    ___.                 
 /  _____/ __ __   ____   ______ _____      ____  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___/ \__  \    /    \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \   / __ \_ |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  > (____  / |___|  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/       \/       \/            \/    \/     \/       
'''
print(guess_a_number)
print("Welcome to guessing number game!")
print("I'm thinking of a number between 1 and 100")
number = random.randint(1, 100)
attempt = 0

while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        attempt = 10
        break
    elif difficulty == 'hard':
        attempt = 5
        break
    else:
        difficulty = input("Wrong input!")

is_game_over = False
while not is_game_over:
    print(f"You have {attempt} attemps remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high.\nGuess again.")
        attempt-=1
    elif guess < number:
        print("Too low.\nGuess again.")
        attempt-=1
    else:
        print(f"You got it. The number is {number}")
        is_game_over = True
    
    if attempt < 1:
        print("You ran out of guesses.")
        is_game_over = True
