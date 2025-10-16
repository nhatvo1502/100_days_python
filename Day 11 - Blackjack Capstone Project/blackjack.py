import random
import os
deck = ['11', '11', '11', '11', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10', 'J', 'J', 'J', 'J', 'J', 'J', 'J', 'J', 'K', 'K', 'K', 'K']

def pick_random_card(aDeck):
    '''Return a random card from a deck and remove that card from the deck'''
    card = random.choice(aDeck)
    aDeck.remove(card)

    return card, aDeck

def card_value(card):
    value = 0
    if card in 'JQK':
        value = 10
    else:
        value = int(card)
    return value

def card_pull(pile, score, aDeck):
    card, aDeck = pick_random_card(aDeck)
    pile.append(card)
    score += card_value(card)
    return pile, score, aDeck

def score_count(pile):
    tempPile = []
    ace = pile.count("11")
    for card in pile:
        tempPile.append(card_value(card))

    if ace <= 1 and (sum(tempPile)-(ace*11)) > 21:
        for i in range(len(tempPile)):
            if tempPile[i] == 11:
                tempPile[i] = 1
    return sum(tempPile)

def compare_card(user_pile, user_score, pc_pile, pc_score):
    print(f"Your final hand: {user_pile}, final score: {user_score}")
    print(f"Computer's final hand: {pc_pile}, final score: {pc_score}")
    if user_score > 21:
        print('You went over. You lose T.T')
    elif pc_score >21:
        print('Computer went over. You win :O')
    elif user_score < pc_score:
        print('You lose =))')
    else:
        print('You win :)')

print("Welcome to blackjack")

playBlackjack = True
def blackJack():
    myDeck = deck
    over21 = False
    user_cards = []
    user_score = 0
    pc_cards = []
    pc_score = 0

    print(len(myDeck))
    for i in range(2):
        user_cards, user_score, myDeck = card_pull(user_cards, user_score, myDeck)
    print(f'Your cards: {user_cards}, current score: {user_score}')
    pc_cards, pc_score, myDeck = card_pull(pc_cards, pc_score, myDeck)
    print(f"Computer's first card: {pc_cards[0]}")    

    userDraw = True
    while userDraw:
        choice = input("Type 'y' to get another card, type 'n' to pass:  ")
        if choice == 'y':     
            user_cards, user_score, myDeck = card_pull(user_cards, user_score, myDeck)
            print(f'Your cards: {user_cards}, current score: {user_score}')
            print(f"Computer's first card: {pc_cards[0]}")
            if user_score > 21:
                over21 = True
                userDraw = False
        elif choice == 'n':
            userDraw = False

    pcDraw = True
    if over21 == True:
        pcDraw = False
        
    while pcDraw:

        while pc_score <= 16:
            pc_cards, pc_score, myDeck = card_pull(pc_cards, pc_score, myDeck)

        while pc_score <= 17 and pc_score <= user_score:
            pc_cards, pc_score, myDeck = card_pull(pc_cards, pc_score, myDeck)
        
        while pc_score <= user_score:
            pc_cards, pc_score, myDeck = card_pull(pc_cards, pc_score, myDeck)
        break
        
    compare_card(user_cards, user_score, pc_cards, pc_score)
    print(f'Original Deck: {len(deck)} ')

os.system('clear')
while True:
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice == 'y':
        blackJack()
    else:
        break

