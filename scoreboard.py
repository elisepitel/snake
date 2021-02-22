from turtle import Turtle
ALIGNEMENT = 'center'
FONT = ("Courier", 18, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.write(f"🧚 Score: {self.score} High Score: {self.high_score}", align=ALIGNEMENT, font=FONT)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"🧚 Score: {self.score} High Score: {self.high_score}", align=ALIGNEMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.update_score()
        self.score = 0

    def increase_score(self):
        self.score += 1
