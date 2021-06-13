from turtle import Turtle


class Score(Turtle):
    """Updating the scoreboard whenever the snake head hits the food"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")  # to make scoreboard visible, by default its black
        self.hideturtle()  # makes turtle hide
        self.write(f"Score: {self.score}", align="center",
                   font=("Fira Code", 12, "bold"))
