def treasure_island():
    isWin = False
    print("Welcome to Treasure Island.\nYour mission is to find the treasure.\nYoure at a cross road. Where do you want to go?")
    user_input = input('       Type "left" or "right"\n')
    if user_input == 'left':
        print("You've come to a lake. There is an island in the middle of the lake.\n")
        user_input = input (' Type "wait" to wait for a boat. Type "swim" to swim across.\n')
        if user_input == 'wait':
            print('You arrive at the island unharmed. There is a house with 3 doors.\n')
            user_input = input(' One red, one yellow, and one blue. Which color do you choose?\n')
            if user_input == 'red':
                print('You die from fire')
            elif user_input == 'yellow':
                print('You found the treasure')
                isWin = True
            elif user_input == 'blue':
                print('You get fucked by a beast')
            else:
                print('You enter the wrong door color you dumbass')
        elif user_input == 'swim':
            print('You get attacked by an angry trout. Game Over')
        else:
            print('You enter the wrong action you dumbass')
    elif user_input == 'right':
        print('You fell into hole and die')
    else:
        print('You enter the wrong direction you dumbass')
    
    return isWin

def game():
    play = 'y'
    win = 0
    lose = 0
    while play == 'y':
        value = treasure_island()
        if value == True:
            win+=1
        else:
            lose+=1
        play = input('Do you want to play again? (y/n) ')
    print(f'You won {win} time(s) out of {win+lose} plays.')

game()