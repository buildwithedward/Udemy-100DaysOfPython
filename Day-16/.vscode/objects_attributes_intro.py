from turtle import Turtle, Screen

jimmy = Turtle()

my_screen = Screen()
print(my_screen.canvwidth)
jimmy.shape("turtle")
jimmy.color("DarkSeaGreen2")
jimmy.pen(fillcolor="black", pencolor="red", pensize=10)
jimmy.left(90)
jimmy.forward(150)
jimmy.right(90)
jimmy.circle(50)
my_screen.exitonclick()
