import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
t.colormode(255)  # setting colormode from 1 to 255


def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


directions = [0, 90, 180, 270]
tim.pensize(10)  # setting the width of pensize
tim.speed(10)  # setting the speed as fast - 10. for fastest - 0

for _ in range(200):
    tim.color(generate_random_color())
    tim.forward(45)
    # Set the orientation of the turtle to to_angle
    tim.setheading(random.choice(directions))
