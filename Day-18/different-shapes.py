from turtle import Turtle, Screen
import random

t = Turtle()

colours = ["orange red", "dark violet", "peru",
           "lime green", "cyan", "deep pink", "indian red"]


def draw_shape(sides):
    angle = 360/sides
    for _ in range(sides):
        t.fd(100)
        t.right(angle)


for shape_sides in range(3, 11):
    t.color(random.choice(colours))
    draw_shape(shape_sides)


s = Screen()
s.exitonclick()
