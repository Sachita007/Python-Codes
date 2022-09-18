from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")

        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_up(self):

        new_y = self.ycor()+10
        self.goto(x=self.xcor(),y =new_y)

    def move_down(self):

        new_y = self.ycor() - 10
        self.goto(x=self.xcor(), y=new_y)

