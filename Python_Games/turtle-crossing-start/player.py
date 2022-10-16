from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        """This function use to move up player by Move_Distance"""
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        """This function use to move Down player by Move_Distance"""
        self.backward(MOVE_DISTANCE)

    def reset_player(self):
        """This return back the player to starting position after completing the level """
        self.goto(STARTING_POSITION)
