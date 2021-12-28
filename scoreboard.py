from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        with open("level.txt") as f:
            self.high_level = int(f.read())
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} Highest Level: {self.high_level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        if self.high_level < self.level:
            self.high_level = self.level
            with open("level.txt", mode="w") as f:
                f.write(f"{self.high_level}")
        self.level = 1
        self.update_scoreboard()
