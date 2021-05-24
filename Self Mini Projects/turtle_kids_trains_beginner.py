import turtle as turtle_module
import random

ed = turtle_module.Turtle()
ed.speed("fast")
ed.pen(pensize=5, fillcolor="IndianRed3")
carriage_nos = int(input("how many carriages do u want in Kids train: "))

ed.hideturtle()
ed.penup()
ed.seth(185)
ed.fd(400)
ed.pendown()


def wheel():
    ed.begin_fill()
    ed.circle(25)
    ed.end_fill()
    ed.seth(0)
    ed.fd(100)
    ed.seth(180)
    ed.begin_fill()
    ed.circle(25)
    ed.end_fill()


def carriage(numbers):
    for _ in range(numbers):
        wheel()
        ed.seth(90)
        ed.fd(100)
        ed.seth(180)
        ed.fd(100)
        ed.seth(270)
        ed.fd(100)
        ed.seth(0)
        ed.fd(175)
        ed.seth(180)


carriage(carriage_nos)
wheel()
ed.seth(90)
ed.fd(25)
ed.seth(130)
ed.fd(60)
ed.seth(90)
ed.fd(30)
ed.seth(180)
ed.fd(75)
ed.seth(270)
ed.fd(100)

screen = turtle_module.Screen()
screen.exitonclick()
