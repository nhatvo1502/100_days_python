from turtle import Screen
from ball import Ball
Y = 390
Y_ = -390
X = 590
X_ = -590

screen = Screen()
screen.setup(1200,800)
screen.bgcolor("black")
ball = Ball()

while True:
    ball.move()

    if ball.xcor() > X or ball.xcor() < X_ or ball.ycor() > Y or ball.ycor() < Y_:
        ball.bounce()
    

screen.exitonclick()