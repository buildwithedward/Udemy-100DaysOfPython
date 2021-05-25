from turtle import Turtle, Screen

tuts = Turtle()
tuts.shape("triangle")  # turns the shape of turtle as triangle
tuts.pensize(4)
tuts.color("purple")


def move_forward():
    tuts.forward(10)


def move_bacward():
    tuts.backward(10)


def turn_left():
    new_heading = tuts.heading() + 10
    tuts.seth(new_heading)


def turn_right():
    new_heading = tuts.heading() - 10
    tuts.seth(new_heading)


def clear():
    tuts.clear()
    tuts.penup()  # without this it'll draw line till home co-ordinatines
    tuts.home()
    tuts.pendown()


screen = Screen()
screen.listen()
# input keystroke as key and function
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_bacward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
