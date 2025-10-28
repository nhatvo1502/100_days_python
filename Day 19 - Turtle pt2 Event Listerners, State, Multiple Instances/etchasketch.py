from turtle import Turtle, Screen

terry = Turtle()
screen = Screen()

def move_forwards():
   terry.forward(10)

def move_backwards():
   terry.backward(10)

def counter_clockwise():
   terry.left(30)

def clockwise():
   terry.right(30)

def clear_screen():
   terry.clear()
   terry.penup()
   terry.home()
   terry.pendown()

   
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()