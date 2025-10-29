from turtle import Turtle, Screen
from tkinter import messagebox, Tk
import random

screen = Screen()
screen.setworldcoordinates(0, 0, 600, 600)
screen.isFood = False

PAUSE = False
DELAY = 100

# construct world
def create_snake(brush=False):
    snake = Turtle("square")
    snake.hideturtle()
    snake.pensize(10)
    snake.penup()
    snake.goto(300, 300)
    if brush==True:
        snake.color("white")
    else:
        snake.color("black")
        snake.showturtle()
        snake.trail = []
        snake.length = 10
    return snake

snake = create_snake()
brush = create_snake(brush=True)

# control
def turn_left():
    snake.left(90)

def turn_right():
    snake.right(90)

# def move():
#     snake.pendown()
#     brush.pendown()
#     snake.forward(10)
#     snake.trail.append(snake.pos())
#     print(f"snake.trail={snake.trail}")
#     print(f"snake.length={snake.length}")
#     print(f"brush.pos()={brush.pos()}")
#     if len(snake.trail) > snake.length:
#         brush.goto(snake.trail[0])
#         snake.trail.pop(0)

def move():
    snake.penup()
    snake.forward(10)
    stampid = snake.stamp()
    snake.trail.append(stampid)

    if len(snake.trail) > snake.length:
        snake.clearstamp(snake.trail.pop(0))
    print(f"snake.trail={snake.trail}")
    print(f"snake.length={snake.length}")
    print(f"brush.pos()={brush.pos()}")
    
    
def pause():
    global PAUSE
    if PAUSE == True:
        PAUSE = False
        play()
    else:
        PAUSE = True

# game brain
def play():
    while not PAUSE:
        move()
        if screen.isFood == False:
            make_food(screen)
        
        if snake.pos()[0] > 591 or snake.pos()[0] < 0 or snake.pos()[1] > 591 or snake.pos()[0] < 0 or snake.pos() in snake.trail:
            end()
            break

def make_food(screen):
    x = random.randint(10, 590)
    y = random.randint(10, 590)
    food = Turtle()
    food.hideturtle()
    food.color("red")
    food.shape("square")
    food.shapesize(1)
    food.teleport(x, y)
    food.showturtle()
    screen.isFood = True

def end():
    root = Tk()
    root.withdraw()
    messagebox.showinfo('Game Over',f"You died! Your snake was {snake.length}m")
    PAUSE = True



screen.listen()
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="Escape", fun=pause)
play()



screen.exitonclick()