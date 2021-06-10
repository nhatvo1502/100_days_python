import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rockR = '''
             ______
           (____   '---
          (_____)
          (_____)
          (____)
            (___)__.---
'''
paperR = '''
             _______
       ____(____    '---
      (______
       (_______
        (_______
         (__________.---
'''
scissorsR = '''
               ______
         ____(____   '---
        (______ 
       (__________
             (____)
              (___)__.---
'''

hand = [rock, paper, scissors]
handR = [rockR, paperR, scissorsR]

print("Welcome to Rock Paper Scissor game!")
while True:
    while True:
        choice = input("Rock, Paper, or Scissor? Enter r, p, or s: ")
        choice=choice.lower()
        if choice=="r":
            i = 0
            break
        elif choice=="p":
            i = 1
            break
        elif choice=="s":
            i = 2
            break

    player_hand = handR[i]
    print(player_hand)

    tidehunter_hand = hand[random.randint(0, 2)]
    print(tidehunter_hand)

    def play(hand1, hand2):
        if hand1==hand2:
            print("Tie")
        elif hand1==rock and hand2==paper:
            print("Lose!")
        elif hand1==rock and hand2==scissors:
            print("Win!")
        elif hand1==paper and hand2==rock:
            print("Win!")
        elif hand1==paper and hand2==scissors:
            print("Lose!")
        elif hand1==scissors and hand2==rock:
            print("Lose!")
        elif  hand1==scissors and hand2==paper:
            print("Win!")
            
    play(hand[i], tidehunter_hand)
    
    keepplaying = input("Play again? y/n ")
    keepplaying=keepplaying.lower()
    if keepplaying=="n":
        break
    else:
        continue
    