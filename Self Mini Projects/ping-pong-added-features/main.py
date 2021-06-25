from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.title("ping pong")
screen.bgcolor("black")
screen.tracer(0)

r_pad = Paddle((390, 0))
l_pad = Paddle((-390, 0))
ping_ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(r_pad.move_up, "Up")
screen.onkey(r_pad.move_down, "Down")
screen.onkey(l_pad.move_up, "w")
screen.onkey(l_pad.move_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ping_ball.ballspeed)
    ping_ball.move()

    if ping_ball.ycor() > 280 or ping_ball.ycor() < -280:
        ping_ball.wall_collision()

    if ping_ball.xcor() > 350 and ping_ball.distance(r_pad) < 50 or ping_ball.xcor() < -350 and ping_ball.distance(l_pad) < 50:
        ping_ball.pad_collison()

    # if right paddle misses
    if ping_ball.xcor() > 390:
        ping_ball.reset_ball()
        score.l_point()

    # if left paddle misses
    if ping_ball.xcor() < -390:
        ping_ball.reset_ball()
        score.r_point()

    if score.l_score == 5 or score.r_score == 5:
        game_on = False
        score.game_over()

screen.exitonclick()
