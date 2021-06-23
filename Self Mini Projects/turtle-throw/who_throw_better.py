# import the necessary libraries
from turtle import Turtle, Screen
import random

# Create custom screen
screen = Screen()
screen.setup(width=600, height=500)
guess = screen.textinput(title="Who will throw better",
                         prompt="Guess which turtle will throw longer distance?")
colors = ["red", "orange", "blue", "green", "purple"]

turtles = []
y_positions = [-85, -60, -35, -10, 15, 40, 65]

# Create multiple turtles and ask them to throw

for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-285, y=y_positions[turtle_index])
    turtles.append(new_turtle)

# Check whether user given guessed color as input
dist = {}

if guess:
    for turtle in turtles:
        rand_throw = random.randint(0, 500)
        turtle.fd(rand_throw)
        dist[turtle.pencolor()] = rand_throw
        winning_turtle = max(dist, key=dist.get)
        winning_dist = max(dist.values())
    if winning_turtle == guess:
        print(
            f"you've won! The winning turtle is {winning_turtle} with covered distance of {winning_dist}")
    else:
        print(
            f"you've lost! The winning turtle is {winning_turtle} with covered distance of {winning_dist}")


# Show results to the user whether he guessed right or wrong


screen.exitonclick()
