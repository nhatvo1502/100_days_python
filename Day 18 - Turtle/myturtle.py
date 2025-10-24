from turtle import Turtle, Screen

jim = Turtle()

jim.shape("turtle")
jim.color("red")

side_length = 100
side_number = 3
# while True:
#     for i in range(side_number):
#         jim.forward(side_length)
#         jim.right(180/side_number)
#     side_number+=1
for a in range(10):
    for i in range(side_number):
            angle = 180-(((side_number-2)*180)/side_number)
            jim.forward(side_length)
            jim.right(angle)
    side_number+=1

screen = Screen()
screen.exitonclick()