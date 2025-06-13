from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down, "s")

game_is_on=True
while game_is_on:

    ball.move()
    time.sleep(ball.time_delay)
    screen.update()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.bounce_y()

    #detect collision with paddle
    # if (((r_paddle.ycor()-50)<ball.ycor()<(r_paddle.ycor()+50) and ball.xcor()==330) or
    #       ((l_paddle.ycor()-50)<ball.ycor()<(l_paddle.ycor()+50) and ball.xcor()==-330)):
    if (ball.distance(r_paddle)<50 and ball.xcor()>330) or (ball.distance(l_paddle)<50 and ball.xcor()>-330):
        ball.bounce_x()

    #right side misses
    if ball.xcor()>380:
        ball.reset_pos()
        score.l_point()
    #left side misses
    if ball.xcor()<-380:
        ball.reset_pos()
        score.r_point()



screen.exitonclick()