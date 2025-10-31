from turtle import Turtle
import random
DISTANT = 20

class Ball(Turtle):
    def __init__(self):
        super().__init__("square")
        self.color("white")
        self.penup()
        self.setheading(random.randint(45, 90))

    def move(self):
        self.forward(DISTANT)

    def bounce(self):
        if self.heading() > 180:
            self.setheading(360-self.heading())
        else:
            self.setheading(180-self.heading())