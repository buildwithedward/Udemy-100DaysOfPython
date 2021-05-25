from turtle import Turtle, Screen

tuts = Turtle()


def move_forward():
    tuts.forward(10)


screen = Screen()
screen.listen()
# input keystroke as key and function
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()
