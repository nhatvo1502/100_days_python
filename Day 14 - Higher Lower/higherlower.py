import random
from game_data import data
logo = r'''
 _     _  _____ _     _____ ____  _     ____  _      _____ ____ 
/ \ /|/ \/  __// \ /|/  __//  __\/ \   /  _ \/ \  /|/  __//  __\
| |_||| || |  _| |_|||  \  |  \/|| |   | / \|| |  |||  \  |  \/|
| | ||| || |_//| | |||  /_ |    /| |_/\| \_/|| |/\|||  /_ |    /
\_/ \|\_/\____\\_/ \|\____\\_/\_\\____/\____/\_/  \|\____\\_/\_\
                                                                
'''
vs = r'''
 _     ____ 
/ \ |\/ ___\
| | //|    \
| \// \___ |
\__/  \____/
                                   
'''

def pick_person():
   return random.choice(data)

def more_fllower(A, B):
   if A["follower_count"] > B["follower_count"]:
      return 'A'
   else:
      return 'B'

def game():
   isRight = True
   score = 0
   while isRight:
      person_A = pick_person()
      person_B = pick_person()
      print(logo)
      print(f"Compare A: {person_A['name']}, {person_A['description'], {person_A['country']}}")
      print(vs)
      print(f"Compare B: {person_B['name']}, {person_B['description'], {person_B['country']}}")
      if score > 0:
         print(f"You are right. Current score: {score}")
      answer = input("Who as more followers? Type 'A' or 'B': ")
      
      if answer == more_fllower(person_A, person_B):
         score+=1
      else:
         isRight = False
         print(logo)
         print(f"Sorry, that's wrong. Final score: {score}")
game()