import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG GAME")
scoreboard = Scoreboard()
screen.tracer(0)

paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(paddle1.move_down, "Down")
screen.onkey(paddle1.move_up, "Up")

screen.onkey(paddle2.move_down, "s")
screen.onkey(paddle2.move_up, "w")

game_is_on = True
speed = 0.1

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detecting collisition
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    #detect collition with right paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()

    speed *=0.1

screen.exitonclick()