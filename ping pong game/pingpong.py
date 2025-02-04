from turtle import Screen


from paddle import Puddle
from Ball import Ball
import time
from Scoreboard import Scoreboard



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

screen.tracer(0)

puddle = Puddle(350)
l_puddle = Puddle(-350)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(puddle.goUp, "Up")
screen.onkey(puddle.goDown, "Down")

screen.onkey(l_puddle.goUp, "w")
screen.onkey(l_puddle.goDown, "s")
gameISon = True
while gameISon:
    time.sleep(0.05)
    screen.update()
    ball.moveball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.odbicY()

    if ball.distance(puddle) < 50 and ball.xcor() > 320 or ball.distance(l_puddle) < 50 and ball.xcor() < -320:
        ball.odbicX()

    if ball.xcor() > 380:
        ball.resetposition()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.resetposition()
        scoreboard.p_point()


screen.exitonclick()