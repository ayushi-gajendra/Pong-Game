# ------------------- Import Modules ------------------- #
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# ------------------- Screen Setup ------------------- #
screen = Screen()
screen.setup(width=800, height=600)         # Set screen size
screen.bgcolor("black")                     # Background color
screen.title("Pong")                        # Window title
screen.tracer(0)                            # Turn off auto refresh

# ------------------- Game Object Initialization ------------------- #
r_paddle = Paddle((350, 0))                 # Right paddle
l_paddle = Paddle((-350, 0))                # Left paddle
ball = Ball()                               # Ball
score = Scoreboard()                        # Scoreboard

# ------------------- Key Bindings ------------------- #
screen.listen()
screen.onkey(r_paddle.go_up, "Up")          # Right paddle up
screen.onkey(r_paddle.go_down, "Down")      # Right paddle down
screen.onkey(l_paddle.go_up, "w")           # Left paddle up
screen.onkey(l_paddle.go_down, "s")         # Left paddle down

# ------------------- Game Loop ------------------- #
game_is_on = True
while game_is_on:
    ball.move()                             # Move the ball
    time.sleep(ball.time_delay)             # Control ball speed
    screen.update()                         # Refresh screen

    # ----------- Wall Collision Detection ----------- #
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # ----------- Paddle Collision Detection ----------- #
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()

    # ----------- Right Paddle Missed ----------- #
    if ball.xcor() > 380:
        ball.reset_pos()
        score.l_point()

    # ----------- Left Paddle Missed ----------- #
    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()

# ------------------- Exit on Click ------------------- #
screen.exitonclick()
