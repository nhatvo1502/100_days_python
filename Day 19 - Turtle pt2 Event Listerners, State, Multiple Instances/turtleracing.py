from turtle import Turtle, Screen
from tkinter import messagebox, Tk
import random

colors = ['red', 'blue', 'green']

def create_turtles():
    khoa = Turtle()
    terry = Turtle()
    nhat = Turtle()
    turtles = [khoa, terry, nhat]
    
    for i in range(0, 3):
        turtle = turtles[i]
        turtle.shape('turtle')
        turtle.color(colors[i])
        turtle.shapesize(2, 2)
    
    return turtles

# Transit turtles to starting
def set_starting_point(turtles):
    distant = 600/(len(turtles) -1)
    for _ in range(0, len(turtles)):
        pos = -300 + _*distant
        turtles[_].penup()
        turtles[_].goto(-500, pos)
        print(len(turtles))
        print(_)
        print(turtles[_].pos())

# Race
def race(turtles):
    current_winner = Turtle()
    current_winner.hideturtle()
    current_winner.penup()
    current_winner.goto(-500, 400)
    isWin = False
    while not isWin:
        for turtle in turtles:
            turtle.forward(random.randint(0, 5))
            print(turtle.pos()[0])
            if turtle.pos()[0] >= 300:
                isWin = True
                return turtle

def annouce_winner(winner, user_predict):
    root = Tk()
    root.withdraw()
    if user_predict == winner.color():
        messagebox.showinfo('Race result',f"{winner.color()[1]} crossed the finish line, you won!")
    else:
        messagebox.showinfo('Race result', f"{winner.color()[1]} crossed the finish line, you lose!")

def main():
    random.shuffle(colors)
    
    turtles = create_turtles()

    screen = Screen()
    set_starting_point(turtles)
    isCorrected = False
    user_bet = screen.textinput('title', 'Which turtle do you bet on? (blue, red, green)')
    while not isCorrected:  
        if user_bet == 'blue' or user_bet == 'red' or user_bet == 'green':
            isCorrected = True
        else:
            user_bet = screen.textinput('tittle', 'Incorrected input! Which turtle do you bet on? (blue, red, green)')
    winner = race(turtles)
    print(f'The winner is {winner.color()[1]}')
    winner.write(f'I win! fuck you guys')
    turtles.remove(winner)
    for _ in turtles:
        _.write(f'aww shit')

    annouce_winner(winner, user_bet)

    screen.exitonclick()

main()