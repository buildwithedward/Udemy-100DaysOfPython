from turtle import Turtle
# Initiating constant values at the top
ALIGNMENT = "center"
FONT = ("Fira Code", 16, "bold")


class Score(Turtle):
    """Updating the scoreboard whenever the snake head hits the food"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")  # to make scoreboard visible, by default its black
        self.penup()  # hiding traces of turtle
        self.goto(0, 270)  # moving the scoreboard at the top of screen
        self.hideturtle()  # makes turtle hide
        self.update_score()  # shows updated score

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        """shows to the user that the game is over"""
        self.goto(0, 0)  # go to (0,0) position
        self.write(f"GAME OVER", align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        """updating scoreboard whenever turtle eats food"""
        self.score += 1
        self.clear()  # clears previous score and updates new one
        self.update_score()
