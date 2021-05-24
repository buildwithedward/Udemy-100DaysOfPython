import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed('fastest')
tim.width(2)  # changing pensize as 1
########### Challenge 5 - Spirograph ########


def draw_spirograph(size_gap):
    """draw spirograph based on fixed size gap"""
    for _ in range(int(360/size_gap)):  # range only accepts whole number
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()  # displays current heading position (0,0)
        tim.seth(current_heading + size_gap)


draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()
