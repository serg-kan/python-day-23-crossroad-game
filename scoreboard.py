from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.goto(-230, 250)

        self.level = 1

    def update_level(self):
        self.level += 1

    def print_level(self):
        self.clear()
        self.write(f"Level {self.level}", move=False, align="center", font=FONT)

    def print_game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align="center", font=FONT)


