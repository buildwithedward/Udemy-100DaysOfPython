from turtle import Turtle
import random


class Ball(Turtle):
    """Creating Ball turtle and moving it"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """When game starts, ball move in different direction"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1  # new_y = self.ycor() - self.y_move

    def paddle_bounce(self):
        self.x_move *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.paddle_bounce()
