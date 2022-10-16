
from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(x=-210, y=260)
        self.score_board()

    def score_board(self):
        """Displaying scoreboard"""
        s_board = f"Level: {self.score}"
        self.write(arg=s_board, move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Display GAME OVER """
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def refresh_score(self):
        """Refresh score on score_board """
        self.score += 1
        self.clear()
        self.score_board()
