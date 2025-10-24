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
directions = [0, 90, 180, 270]
jim.shape("turtle")
jim.color("red")

side_length = 30
side_number = 3
angle = 90
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

# for i in range(20):
#     random_color()
#     draw_shape(side_number)
#     side_number+=1

def random_walk(angle):
    jim.pensize(10)
    jim.speed(0)
    for i in range(1000):
        random_color()
        jim.forward(side_length)
        turn = random.randint(0, 4)
        if turn == 0:
            jim.right(angle)
        elif turn == 1:
            jim.left(angle)
        elif turn == 2:
            jim.right(180)

def random_walk2():
    jim.pensize(15)
    jim.speed(0)
    for i in range(1000):
        random_color()
        jim.forward(side_length)
        jim.setheading(random.choice(directions))


random_walk2()


screen = Screen()
# screen.exitonclick()
jim.mainloop()