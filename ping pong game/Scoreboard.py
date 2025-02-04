from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.Lscore = 0
        self.Pscore = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.Lscore, align='center', font=('Arial', 80, 'normal'))
        self.goto(100, 180)
        self.write(self.Pscore, align='center', font=('Arial', 80, 'normal'))

    def l_point(self):
        self.Lscore += 1
        self.update()

    def p_point(self):
        self.Pscore += 1
        self.update()