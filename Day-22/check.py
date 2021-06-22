from turtle import Turtle, Screen

tuts = Turtle()
tuts.shape("circle")
tuts.color("white")
tuts.shapesize(stretch_len=1, stretch_wid=1)
tuts.seth(320)
tuts.fd(100)

screen = Screen()
screen.bgcolor("black")


screen.exitonclick()
