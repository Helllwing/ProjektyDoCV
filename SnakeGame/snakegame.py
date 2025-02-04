from turtle import  Screen
import time

from dzien20.snakeclass import gameISon
from snakeclass import Snake
from Foodclass import Food
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor('black')
screen.tracer(0)
screen.setup(600,600)
snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


Gameon = True
while Gameon:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.newfoodpos()
        snake.extendtim()
        scoreboard.updateScore()
        scoreboard.IncreaseScore()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        Gameon = False
        scoreboard.gameOver()

    for tims in snake.tims:
        if tims == snake.head:
            pass
        elif snake.head.distance(tims) < 10:
            Gameon = False
            scoreboard.gameOver()
screen.exitonclick()

