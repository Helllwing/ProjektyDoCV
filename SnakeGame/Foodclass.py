from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('Blue')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")

    def newfoodpos(self):
        ranx = random.randint(-280, 280)
        randy = random.randint(-280, 280)
        self.goto(ranx, randy)