import random
guess_a_number = r'''
  ________                                                    ___.                 
 /  _____/ __ __   ____   ______ _____      ____  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___/ \__  \    /    \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \   / __ \_ |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  > (____  / |___|  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/       \/       \/            \/    \/     \/       
'''
def set_difficulty():
   choice = input("Please select difficulty 'easy' or 'hard':  ")
   if choice == 'easy':
      return 10
   elif choice == 'hard':
      return 5
   else:
      print("Wrong input..")
      return set_difficulty()
   
def check_answer(guess, answer, attempts):
    if guess > answer:
        print("Too high!")
    elif guess < answer:
        print("Too low!")
    else:
        print(f"You got it. The answer is {answer}")
    
    return attempts-1

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    attempts = set_difficulty()
    
    
    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        attempts = check_answer(guess, answer, attempts)

        if attempts == 0:
            print("You ran out of attempts. GG")
            return

game()