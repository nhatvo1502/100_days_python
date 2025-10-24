from turtle import Turtle, Screen
import random

jim = Turtle()

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "pink",
    "brown",
    "black",
    "gray",
    "cyan",
    "magenta",
    "lime",
    "gold",
    "turquoise",
    "violet",
    "indigo",
    "navy",
    "coral",
    "salmon"
]

jim.shape("turtle")
jim.color("red")

side_length = 100
side_number = 3
# while True:
#     for i in range(side_number):
#         jim.forward(side_length)
#         jim.right(180/side_number)
#     side_number+=1

def random_color():
    jim.color(random.choice(colors))

def draw_shape(sides):
    for i in range(sides):
        if i == 0:
            angle = (((sides-2)*180)/sides)
        else:
            angle = 180-(((sides-2)*180)/sides)
        jim.forward(side_length)
        jim.right(angle)

for i in range(20):
    random_color()
    draw_shape(side_number)
    side_number+=1

screen = Screen()
screen.exitonclick()