from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 13, 'normal')


class Scoreboard(Turtle):

    def __init__(self):

        with open("data.txt") as data:
            score = data.read()
            self.high_score = score
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=280)
        self.score_board()

    def score_board(self):
        """Displaying scoreboard"""
        self.clear()
        self.update_data()
        s_board = f"Score: {self.score} High Score: {self.high_score}"
        self.write(arg=s_board, move=False, align=ALIGNMENT, font=FONT)

    def rest_score(self):
        if self.score > int(self.high_score):
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.score_board()


    # def game_over(self):
    #     """Display GAME OVER """
    #     self.goto(x=0, y=0)
    #     self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def refresh_score(self):
        """Refresh score on score_board """
        self.score += 1
        self.score_board()

    def update_data(self):
        with open("data.txt", mode="r") as data:

            score = data.read()
            self.high_score = score
