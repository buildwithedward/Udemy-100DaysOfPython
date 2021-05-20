from turtle import Turtle, Screen

sq = Turtle()
sq.shape("turtle")
sq.color("red")

for _ in range(4):
    sq.forward(100)
    sq.left(90)

screen = Screen()
screen.exitonclick()
