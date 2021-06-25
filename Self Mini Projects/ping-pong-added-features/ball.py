from turtle import Turtle
import random
COLORS = ["pink", "gold", "spring green",
          "salmon", "powder blue", "cyan", "turquoise"]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.ballspeed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def wall_collision(self):
        self.ymove *= -1

    def pad_collison(self):
        self.color(random.choice(COLORS))
        self.xmove *= -1
        self.ballspeed *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.color("white")
        self.ballspeed = 0.1
        self.pad_collison()
