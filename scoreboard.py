from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score_file.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        """ Updated the high score value """
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score_file.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0  # resets the score
        self.update_scoreboard()