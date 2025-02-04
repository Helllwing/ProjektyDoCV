from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 260)
        self.updateScore()

    def updateScore(self):
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'bold'))

    def IncreaseScore(self):
        self.score += 1
        self.clear()
        self.updateScore()

    def gameOver(self):
        self.goto(0, 0)
        self.write(f"Game Over", align='center', font=('Arial', 24, 'bold'))