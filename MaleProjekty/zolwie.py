from random import randint
from turtle import Turtle, Screen

screen = Screen()
user_bet = screen.textinput("do ur gambling",
                            "which turtle is a truly gambler?: red, blue, green, yellow, orange, or purple")

colors = ["red", "blue", "green", "yellow", "orange", "purple"]
tim = Turtle("turtle")
jim = Turtle("turtle")
slim = Turtle("turtle")
john = Turtle("turtle")
luke = Turtle("turtle")
han = Turtle("turtle")

turtles = [tim, jim, slim, john, luke, han]

screen.setup(800, 800)
is_race = False

def Settings(turtle, y, color):
    turtle.penup()
    turtle.goto(-380, y)
    turtle.color(color)

Settings(tim, -200, colors[0])
Settings(jim, -150, colors[1])
Settings(slim, -100, colors[2])
Settings(han, -50, colors[3])
Settings(luke, 0, colors[4])
Settings(john, 50, colors[5])

if user_bet:
    is_race = True

while is_race:
    for turtle in turtles:
        distance = randint(1,10)
        turtle.forward(distance)
        if turtle.xcor() > 380:
            is_race = False
            winningColor = turtle.pencolor()
            if winningColor == user_bet:
                print(f"u've won, {winningColor} is first")
            else:
                print(f"u've lost, {winningColor} is first")
            winner_circle = Turtle()
            winner_circle.shape("circle")
            winner_circle.shapesize(3, 3)
            winner_circle.color(winningColor)
            winner_circle.penup()
            winner_circle.goto(0, 150)
            break

screen.exitonclick()
