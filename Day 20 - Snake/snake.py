from turtle import Turtle, Screen

screen = Screen()
screen.setworldcoordinates(0, 0, 600, 600)

PAUSE = False

def create_snake(brush=False):
    snake = Turtle("square")
    snake.hideturtle()
    snake.pensize(10)
    snake.penup()
    snake.goto(300, 300)
    if brush==True:
        snake.color("lime")
    else:
        snake.color("black")
        snake.showturtle()
        snake.trail = []
        snake.length = 10
    return snake

snake = create_snake()
brush = create_snake(brush=True)

def turn_left():
    snake.left(90)

def turn_right():
    snake.right(90)

def move():
    snake.pendown()
    brush.pendown()
    snake.forward(10)
    snake.trail.append(snake.pos())
    print(f"snake.trail={snake.trail}")
    print(f"snake.length={snake.length}")
    print(f"brush.pos()={brush.pos()}")
    if len(snake.trail) > snake.length:
        brush.goto(snake.trail[0])
        snake.trail.pop(0)

def pause():
    global PAUSE
    if PAUSE == True:
        PAUSE = False
        play()
    else:
        PAUSE = True
        

def play():
    while not PAUSE:
        move()

screen.listen()
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="Escape", fun=pause)
play()



screen.exitonclick()