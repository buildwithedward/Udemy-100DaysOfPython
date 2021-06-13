from turtle import Turtle
import random


class Food(Turtle):  # Inheriting everything from Turtle class

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # making turtle 10X10 size
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()  # randomly sets food particle on screen

    def refresh(self):
        """Set food to new location when snake head collided with food"""
        # screen size 300X300 dont want snake to hit wall
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
