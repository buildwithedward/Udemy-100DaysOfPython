import turtle as t
import random

# colorlist is in rgb value. So change colormode in rgb
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()  # removes turtle direction while dotting
tim.hideturtle()  # hides turtle in screen

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145,
                                                                                                                                                                                            178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

# to display all the points we are moving heading
tim.seth(225)
tim.fd(300)
tim.seth(0)

no_counts = 100

for dot_count in range(1, no_counts + 1):
    tim.dot(20, random.choice(color_list))
    tim.fd(50)

    if dot_count % 10 == 0:  # after every 10th dot it'll turn direction
        tim.seth(90)
        tim.fd(50)
        tim.seth(180)
        tim.fd(500)
        tim.seth(0)

screen = t.Screen()
screen.exitonclick()
