from turtle import Turtle


class Score(Turtle):
    """Creates scorebard and increases score if opposite paddle misses the ball"""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        """Create & Display scoreboard on left and right side"""
        self.clear()  # used to clear previous score and update latest one
        self.goto(-100, 200)
        self.write(self.l_score, align="center",
                   font=("Arial", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center",
                   font=("Arial", 50, "normal"))

    def l_point(self):
        """Update left scoreboard if right paddle misses ball"""
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
