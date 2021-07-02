from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        """display updated score"""
        self.clear()
        self.goto(-270, 270)
        self.write(f"Level {self.score}", align="left", font=FONT)

    def score_point(self):
        """increases score when turtle crosses each level"""
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
