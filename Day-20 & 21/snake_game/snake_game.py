from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)  # customizing screensize
screen.bgcolor("black")
screen.title("Traditional Snake Game")
screen.tracer(0)

# 1. Creating Snake body
snake = Snake()
screen.listen()

# 3. Moving the snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# 2.Moving Snake
is_game_on = True

while is_game_on:
    screen.update()  # updating the screen
    time.sleep(0.1)  # making the turtle speed delay
    snake.move()

screen.exitonclick()
