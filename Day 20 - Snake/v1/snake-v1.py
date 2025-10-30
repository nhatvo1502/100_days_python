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
    snake.pensize(5)
    snake.penup()
    snake.goto(300, 300)
    if brush==True:
        snake.color("white")
    else:
        snake.color("black")
        snake.showturtle()
        snake.stampid = []
        snake.trail = []
        snake.length = 10
    return snake

snake = create_snake()

# control
def turn_left():
    snake.setheading(180)

def turn_right():
    snake.setheading(0)

def up():
    snake.setheading(90)

def down():
    snake.setheading(270)

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
    snake.stampid.append(stampid)
    snake.trail.append(snake.pos())

    if len(snake.stampid) > snake.length:
        snake.clearstamp(snake.stampid.pop(0))
        snake.trail.pop(0)
    print(f"snake.stampid={snake.stampid}")
    print(f"snake.trail={snake.trail}")
    print(f"snake.length={snake.length}")
    
    
def pause():
    global PAUSE
    if PAUSE == True:
        PAUSE = False
        play()
    else:
        PAUSE = True

def check_wall():
    if snake.pos()[0] > 591 or snake.pos()[0] < 0 or snake.pos()[1] > 591 or snake.pos()[0] < 0:
        end()
        return True
    return False

def check_body():
    if snake.pos() in snake.trail[:-1]:
        end()
        return True
    return False

def check_food():
    if snake.pos() in screen.food.hitbox:
        screen.food.clear()
        screen.food.hideturtle()
        screen.isFood = False
        snake.length+=1

# game brain
def play():
    while not PAUSE:
        move()
        if screen.isFood == False:
            make_food(screen)
        print(f"screen.food.pos()={screen.food.pos()}")
        print(f"snake.pos()={snake.pos()}")
        isWalled = check_wall()
        isBodied = check_body()
        if isWalled == True or isBodied == True:
            break
        check_food()
        
def make_food(screen):
    x = random.randint(10, 590)
    y = random.randint(10, 590)
    screen.food = Turtle()
    screen.food.hideturtle()
    screen.food.color("red")
    screen.food.shape("square")
    screen.food.shapesize(1)
    screen.food.teleport(x, y)
    screen.food.showturtle()
    screen.isFood = True
    screen.food.hitbox = []
    for x_ in range(x-10, x+10):
        for y_ in range(y-10, y+10):
            tup = (x_, y_)
            screen.food.hitbox.append(tup)
    print(f"food.hitbox={screen.food.hitbox}")
    

def end():
    root = Tk()
    root.withdraw()
    messagebox.showinfo('Game Over',f"You died! Your snake was {snake.length}m")
    PAUSE = True



screen.listen()
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Escape", fun=pause)
screen.onkey(key="Up", fun=up)
screen.onkey(key="Down", fun=down)
play()



screen.exitonclick()