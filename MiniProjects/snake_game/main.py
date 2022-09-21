from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=580, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)    # Tracer function is used to turn the turtle animation ON or OFF

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()                               # used to detect key press
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food and extend snake
    if snake.head.distance(food) < 15:
        food.refresh()
        score.refresh_score()
        snake.extend()

    # Detect collision with wall and end thw game
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset_snake()
        score.rest_score()

    # Detect collision with tail
    # if head collides with any segment in the tail : trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            snake.reset_snake()
            score.rest_score()

screen.exitonclick()
