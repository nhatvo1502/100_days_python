from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
        
    def add(self):
        self.clear()
        self.score+=1
        self.update_scoreboard()
    
    def clear(self):
        super().clear()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT,  font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)