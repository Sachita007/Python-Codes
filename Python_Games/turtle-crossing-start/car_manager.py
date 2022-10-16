import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.moving_distance = STARTING_MOVE_DISTANCE



    def make_car(self):
        """This function used to make random color cars"""
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            random_y = random.randint(-250, 250)
            starting_x = 280
            car.setheading(180)
            car.goto(x=starting_x, y=random_y)
            self.cars.append(car)

    def car_move(self):
        """This function used to move car in random interval of time"""

        for car in self.cars:
            car.forward(self.moving_distance)
            if car.xcor() <=-280:
                car.color("white")
                self.cars.remove(car)

    def increase_speed(self):
        """THis function used to increase speed of cars by Move_Increment"""
        self.moving_distance += MOVE_INCREMENT










