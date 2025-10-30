from turtle import Turtle
import time

STARTING_POSITIONS = [(-40, 0), (-20, 0), (0, 0)]

class Snake:
    def __init__(self, screen):
        self.segments = []
        self.create_snake()
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
        
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto((new_x, new_y))
        self.segments[0].forward(20)
        
    def turn_left(self):
        self.left(90)

    def turn_right(self):
        self.right(90)