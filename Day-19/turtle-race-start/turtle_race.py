from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=500)  # make custom screen
user_input = screen.textinput(title="Make a bet.",
                              prompt="Which turtle wll win the race? Enter a color: ")

colors = ["deep pink", "crimson", "purple",
          "dark orange", "sea green", "deep sky blue"]
y_positions = [-85, -60, -35, -10, 15, 40, 65]
all_turtle = []  # to append each new turtle in the list


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()  # penning up as we dont wanna see turtle lines while moving
    new_turtle.color(colors[turtle_index])
    # moving the turtle to end of the window
    new_turtle.goto(x=-285, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_input:  # checks whether the user decided the winning turtle
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:  # each turtle in list would be randomly moved
        if turtle.xcor() > 280:  # 300 -40/2, 40 - size of the turtle
            is_race_on = False  # game completed once turtle reaches the end
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_input:
                print(f"You've Won!,The winning turtle is {winning_turtle} ")
            else:
                print(
                    f"Sorry, your turtle have lost. The winning turtle is {winning_turtle}")
        rand_dist = random.randint(0, 10)  # generates random distance to move
        turtle.forward(rand_dist)

screen.exitonclick()
