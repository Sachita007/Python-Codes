from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(position=(350, 0))
l_paddle = Paddle(position=(-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()  # used to detect key press
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.ball_move()

    # --Detect collision from ball and make ball bounce
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # --Detect collision from paddle and make ball bounce
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # --Detect the ball is missed by Right paddle
    if ball.xcor()>400:
        ball.reset_position()
        scoreboard.l_point()

    #  --Detect the ball  is missed by Left paddle
    if ball.xcor()<-400:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()
