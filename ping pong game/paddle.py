from turtle import Turtle




class Puddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.createpuddle(position)

    def createpuddle(self, position):
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position, 0)

    def goUp(self):
        newY = self.ycor() + 20
        self.goto(self.xcor(), newY)


    def goDown(self):
        newY = self.ycor() - 20
        self.goto(self.xcor(), newY)