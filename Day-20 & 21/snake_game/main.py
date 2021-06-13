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
        snake.extend()
        score.increase_score()

    # Detect collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    # Detect collision with tail
    # if snake head collides any part of segment, then game over

    for segment in snake.segments[1:]:
        # first segment snake head, excluding it, will satisfy the below if condition
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()


screen.exitonclick()
