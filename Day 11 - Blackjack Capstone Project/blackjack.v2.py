
import random
beautifulDeck = ['11', '11', '11', '11', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10', 'J', 'J', 'J', 'J', 'J', 'J', 'J', 'J', 'K', 'K', 'K', 'K']
deck = []
# Reset deck
def reset_deck():
    global beautifulDeck, deck
    deck = beautifulDeck.copy()

# Create a deal card function that return a random card
def deal_card():
    card = random.choice(deck)
    return card

# Create a function called calculate_score() return sum
# Check for blackjack (ace + 10), return 0 instead of actual score
# 
def calculate_score(cards):
    # convert cards to int
    temp_cards = []
    for i in range(len(cards)):
        if cards[i] in 'JQK':
            temp_cards.append(10)
        else:
            temp_cards.append(int(cards[i]))

    # Check blackjack
    if sum(temp_cards) == 21 and len(temp_cards) == 2:
        return 0
    
    # When ace = 1    
    if 11 in cards and sum(temp_cards) > 21:
         temp_cards.remove(11)
         temp_cards.append(1)
    
    return sum(temp_cards)


def blackjack():
    user_cards = []
    computer_cards = []
    reset_deck()
    # Deal user and computer 2 cards each and append() to their piles
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, your current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = 'y'
        while user_should_deal == 'y':
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:  ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                print(f"Your cards: {user_cards}, your current score: {user_score}")
                print(f"Computer's first card: {computer_cards[0]}")
            
            if user_score > 21:
                user_should_deal = 'n'

    while computer_score != 0 and computer_score <17 and computer_score < user_score:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f'Your cards: {user_cards}, your final score {user_score}')
    print(f'Computer cards: {computer_cards}, computer final score {computer_score}')

    if user_score > 21:
        print('You went over. You lose!')
    elif computer_score > 21:
        print('Computer went over. You win!')
    elif computer_score > user_score:
        print('Computer win!')
    elif user_score > computer_score or user_score == 0:
        print('You win!')
    else:
        print('Idk what the f is this scenario')

while True:
    choice = input('Do you want to play blackjack (y/n): ')
    if choice == 'y':
        blackjack()
    else:
        break
