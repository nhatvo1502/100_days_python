from turtle import Turtle, Screen
from tkinter import messagebox, Tk
import random

COLORS = [
    "red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "black", "gray", "cyan", "magenta", "gold", "silver", "coral", "turquoise", "lime", "navy", "maroon",
    "olive", "teal", "aqua", "indigo", "violet", "khaki", "salmon", "plum", "orchid",
    "tan", "tomato", "chocolate", "crimson", "lavender", "azure", "peru", "seagreen", "slateblue", "skyblue",
    "darkgreen", "darkred", "darkblue", "darkorange", "darkviolet", "darkgray", "deepskyblue", "lightgreen", "lightblue", "lightcoral",
    "lightpink", "lightsalmon", "lightgray", "lightcyan", "mediumblue", "mediumseagreen", "mediumvioletred", "royalblue", "sienna"
]
FINISH_LINE = 400

def create_turtles(num):
    random.shuffle(COLORS)
    turtles = []
    color_index = []
    for turtle_index in range(0, num):
        jennie = Turtle()
        jennie.shape('turtle')
        jennie.color(COLORS[turtle_index])
        color_index.append(COLORS[turtle_index])
        jennie.shapesize(2, 2)
        turtles.append(jennie)
    
    return turtles, color_index

# Transit turtles to starting
def set_starting_point(turtles, color_index):
    distant = 600/(len(turtles) -1)
    for _ in range(0, len(turtles)):
        pos = -300 + _*distant
        turtles[_].penup()
        turtles[_].goto(-500, pos)
        print(len(turtles))
        print(_)
        print(turtles[_].pos())
        turtles[_].write(f"                 {turtles[_].color()[1]}")
    
    return turtles, color_index

def prompt_turtle_number(screen):
    tur_num = 0
    while tur_num < 2 or tur_num > 10:
        tur_num = screen.numinput('turtle number', "Enter the number of turles between 1-10: ")
    return int(tur_num)

def make_bet(screen, color_index):
    isCorrected = False
    color_selection = ', '.join(color_index)
    user_bet = screen.textinput('title', f'Which turtle do you bet on? ({color_selection})')
    while not isCorrected:  
        if user_bet.lower() in COLORS:
            isCorrected = True
        else:
            user_bet = screen.textinput('tittle', f'Incorrected input! Which turtle do you bet on? ({color_selection})')
    return user_bet

def play_again(screen):
    isCorrected = False
    user_input = screen.textinput('tittle', f'Do you want to play again? (y/n) ')
    while not isCorrected:
        if user_input.lower() == 'y':
            isCorrected = True
            return True
        elif user_input.lower() == 'n':
            isCorrected = True
            return False
        else:
            user_input = screen.textinput('tittle', f'Wrong input! Do you want to play again? (y/n) ')

# Race
def race(turtles):
    for turtle in turtles:
        turtle.clear()
    isWin = False
    while not isWin:
        for turtle in turtles:
            turtle.forward(random.randint(0, 5))
            print(turtle.pos()[0])
            if turtle.pos()[0] >= FINISH_LINE:
                isWin = True
                turtle.write(f"                 {turtle.color()[1]}")
                return turtle

def check_win(winner, user_predict, score, round):
    root = Tk()
    root.withdraw()
    round+=1
    if user_predict == winner.color()[1]:
        messagebox.showinfo('Race result',f"{winner.color()[1]} crossed the finish line, you won!")
        score+=1
        return score, round, True
    else:
        messagebox.showinfo('Race result', f"{winner.color()[1]} crossed the finish line, you lose!")
        return score, round, False
    
def get_score(score, round):
    root = Tk()
    root.withdraw()
    messagebox.showinfo('Score board', f"Your won {score} races out of {round}")

def main():
    score = 0
    round = 0
    screen = Screen()
    
    
    isPlaying = True
    while isPlaying:
        
        turtles_number = prompt_turtle_number(screen)

        turtles, color_index = set_starting_point(*create_turtles(turtles_number))

        user_bet = make_bet(screen, color_index)

        winner = race(turtles)

        score, round, isWin = check_win(winner, user_bet, score, round)

        isPlaying = play_again(screen)
        screen.clearscreen()
    get_score(score, round)
    screen.exitonclick()

main()