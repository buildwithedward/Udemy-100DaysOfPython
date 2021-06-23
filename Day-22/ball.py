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
        self.ball_speed = 0.1

    def move(self):
        """When game starts, ball move in different direction"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1  # new_y = self.ycor() - self.y_move

    def paddle_bounce(self):
        self.x_move *= -1
        self.ball_speed *= 0.9  # increases ball speed whenever it hits paddle

    def reset_pos(self):
        """when paddle misses, go to home and move ball towards another paddle"""
        self.goto(0, 0)
        self.ball_speed = 0.1  # resetting the ball speed back to normal
        self.paddle_bounce()  # reverses direction to another paddle when one paddle misses
