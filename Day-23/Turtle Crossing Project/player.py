from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_turtle()
        self.left(90)

    def move(self):
        """Making turtle to move in forward direction"""
        self.forward(MOVE_DISTANCE)

    def reset_turtle(self):
        """Reset to the initial position"""
        self.goto(STARTING_POSITION)

    def is_turtle_crossed(self):
        """checks if turtle reaches the end of screen"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
