from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from  scoreboard import ScoreBoard
import time

screen = Screen()
screen.listen()

screen.setup(width=1000 , height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


def draw_line():
    tim = Turtle()
    tim.hideturtle()
    tim.pencolor("white")
    tim.pensize(5)
    tim.penup()
    tim.goto(0 , 290)
    tim.setheading(270)
    for _ in range(10):
        tim.pendown()
        tim.forward(30)
        tim.penup()
        tim.forward(30)
draw_line()                       #The middle line

paddle_left = Paddle((-470,0))
paddle_right = Paddle((470,0))
ball = Ball()
scoreboard = ScoreBoard()

screen.onkeypress(paddle_left.move_up , "w")
screen.onkeypress(paddle_left.move_down , "s")
screen.onkeypress(paddle_right.move_up , "p")
screen.onkeypress(paddle_right.move_down , "l")

game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)
    # detecting collision with walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()
    # detecting ball hitting the paddle
    if (ball.distance(paddle_right) < 50 and ball.xcor() >= 440) or (ball.distance(paddle_left) < 50 and ball.xcor() <= -440):
        ball.paddle_hit()
    # ball going out of bound
    if ball.xcor() < -510:             #left missed, right scored
        time.sleep(1)
        ball.reset_position()
        scoreboard.inc_right_score()
    if ball.xcor() > 510:              #right missed, left scored
        time.sleep(1)
        ball.reset_position()
        scoreboard.inc_left_score()


screen.exitonclick()

