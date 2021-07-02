import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tuts = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(tuts.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_cars()
    carmanager.move()
    if tuts.is_turtle_crossed():
        tuts.reset_turtle()
        carmanager.level_up()
        scoreboard.score_point()

    for car in carmanager.cars:
        if car.distance(tuts) < 20:  # car shape (20,40)
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
