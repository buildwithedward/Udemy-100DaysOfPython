from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)  # customizing screensize
screen.bgcolor("black")
screen.title("Traditional Snake Game")
screen.tracer(0)

# 1. Creating Snake body
snake = Snake()
food = Food()  # initialising food as soon as creating snake
score = Score()

# 3. Moving the snake
screen.listen()
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

    # Detect collision with food
    # snake head collision with food at a lesser dist of 15
    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()
