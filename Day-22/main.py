from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Classic Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    # Detect Collision with wall:
    if ball.ycor() > 280 or ball.ycor() < -280:  # Screen size 600
        ball.wall_bounce()

    # Detect collision with Wall and bounce
    # ball doesnt meet the middle point for collision, so we give distance as 50 and captures collision
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.paddle_bounce()

    # Detect if paddle misses the ball
    if ball.xcor() > 380:  # if r_paddle misses
        ball.reset_pos()
        score.l_point()
    if ball.xcor() < -380:  # if l_paddle misses
        ball.reset_pos()
        score.r_point()


screen.exitonclick()
