from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.read_highscore()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_highscore()
        self.score = 0
        self.update_scoreboard()

    def read_highscore(self):
        with open("highscore.txt") as highscore_file:
            highscore = highscore_file.read()
        return int(highscore)

    def write_highscore(self):
        with open("highscore.txt", mode="w") as highscore_file:
            highscore_file.write(str(self.highscore))




    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)


