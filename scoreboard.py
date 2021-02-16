from turtle import Turtle
ALIGNEMENT = 'center'
FONT = ("Courier", 18, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.write(f"🧚 Score: {self.score}", align=ALIGNEMENT, font=FONT)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"🧚 Score: {self.score}", align=ALIGNEMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNEMENT, font=("Courier", 22, "normal"))
