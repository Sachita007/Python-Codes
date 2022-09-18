from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 25, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        """Displaying scoreboard"""
        self.clear()
        self.goto(-200,260)
        self.write(arg=self.l_score, move=False, align=ALIGNMENT, font=FONT)
        self.goto(200, 260)
        self.write(arg=self.r_score, move=False, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score +=1
        self.update_scoreboard()

    def r_point(self):
        self.r_score +=1
        self.update_scoreboard()