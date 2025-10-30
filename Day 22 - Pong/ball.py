from turtle import Turtle
import random
DISTANT = 20

class Ball(Turtle):
    def __init__(self):
        super().__init__("square")
        self.color("white")
        self.penup()

    def move(self):
        self.forward(DISTANT)