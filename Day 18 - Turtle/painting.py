from turtle import Turtle, Screen
import random
colors_list = [(229, 228, 226), (225, 223, 224), (199, 175, 118), (125, 36, 24), (187, 158, 50), (170, 105, 56), (5, 57, 83), (222, 223, 226), (200, 216, 205), (108, 67, 85)]

lisa = Turtle()
lisa.shape("turtle")
screen = Screen()
screen.colormode(255)
screen.setworldcoordinates(-100, -100, 600, 600)
lisa.penup()
lisa.speed(10)

veritcal = 0
for y in range(0, 10):
   lisa.teleport(0, veritcal, fill_gap=False)
   for x in range(0, 10):
      print(lisa.position())
      tup = random.choice(colors_list)
      print(tup)
      lisa.dot(20, tup)
      lisa.forward(50)
   veritcal+=50
lisa.hideturtle()
screen.mainloop()