from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():

    def __init__(self):
        self.cars = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        """Creating new cars everytime with distance gap (random choice condition true)"""
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            cars_create = Turtle(shape="square")
            cars_create.color(random.choice(COLORS))
            cars_create.shapesize(stretch_wid=1, stretch_len=2)
            cars_create.penup()
            random_ycar = random.randint(-250, 250)
            cars_create.goto(300, random_ycar)
            self.cars.append(cars_create)

    def move(self):
        """car movement"""
        for car in self.cars:
            car.backward(self.carspeed)

    def level_up(self):
        self.carspeed += MOVE_INCREMENT
