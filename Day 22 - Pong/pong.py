from turtle import Screen
from ball import Ball

screen = Screen()
screen.setup(1200,800)
screen.bgcolor("black")
ball = Ball()

while True:
    ball.setheading(45)
    ball.move()

screen.exitonclick()