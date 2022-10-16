import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(fun=player.move_up, key="Up")
screen.onkeypress(fun=player.move_down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.make_car()
    car_manager.car_move()

    # --Detecting collision with car
    for car in car_manager.cars:
        if player.distance(car) < 25:
            scoreboard.game_over()
            game_is_on = False

    # --Detecting the player reached the other end
    if player.ycor() >= 270:
        scoreboard.refresh_score()
        car_manager.increase_speed()
        player.reset_player()

screen.exitonclick()
