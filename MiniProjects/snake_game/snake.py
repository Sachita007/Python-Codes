from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """This function create snake body."""
        self.x_coordinate = 0
        for turtle in range(0, 3):
            self.x_coordinate -= 20
            self.add_segment(position=(self.x_coordinate,0))


    def add_segment(self,position):
        """Adding segment of snake body to list """
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """This function used to extend body of snake after eating food"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move function is used to move snake forward"""
        for seg_num in range((len(self.segments) - 1), 0, -1):
            x_cor = self.segments[seg_num - 1].xcor()
            y_cor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=x_cor, y=y_cor)
        self.head.forward(20)

    def up(self):
        """Turning the snake in upward direction """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turning the snake in downward direction """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """Turning the snake in right direction """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """Turning the snake in left direction """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(x=600, y=600)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]