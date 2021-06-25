
from turtle import Turtle
HEIGHT = 240
STEPS = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_up(self):
        if self.ycor() < HEIGHT:
            new_y = self.ycor() + STEPS
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -HEIGHT:
            new_y = self.ycor() - STEPS
            self.goto(self.xcor(), new_y)
