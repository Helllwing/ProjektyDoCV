from turtle import Turtle

positionOfTurtle = [(0,0), (-20, 0), (-40,0)]
gameISon = True
moveDistance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.tims = []
        self.create_tim()
        self.head = self.tims[0]

    def create_tim(self):
        for position in positionOfTurtle:
            self.add_body(position)

    def add_body(self, position):
        tim = Turtle('square')
        tim.color('white')
        tim.penup()
        tim.goto(position)
        self.tims.append(tim)

    def extendtim(self):
        self.add_body(self.tims[-1].position())

    def move(self):
            for BodyNum in range(len(self.tims) - 1, 0, -1):
                new_x = self.tims[BodyNum - 1].xcor()
                new_y = self.tims[BodyNum - 1].ycor()
                self.tims[BodyNum].goto(new_x, new_y)
            self.head.forward(moveDistance)

    def right(self ):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)