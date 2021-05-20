from turtle import Turtle, Screen

t = Turtle()

for _ in range(10):
    t.fd(25)
    t.penup()
    t.fd(10)
    t.pendown()


s = Screen()
s.exitonclick()
