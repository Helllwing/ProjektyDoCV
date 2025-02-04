from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.moveX = 10
        self.moveY = 10

    def moveball(self):
        new_x = self.xcor() + self.moveX
        new_y = self.ycor() + self.moveY
        self.goto(new_x, new_y)

    def odbicY(self):
        self.moveY *= -1

    def odbicX(self):
        self.moveX *= -1

    def resetposition(self):
        self.goto(0, 0)
        self.odbicX()