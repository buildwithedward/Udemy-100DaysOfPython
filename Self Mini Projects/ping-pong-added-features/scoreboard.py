from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()  # clears previous score
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        # self.winner_announce()

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=("Arial", 45, "normal"))
