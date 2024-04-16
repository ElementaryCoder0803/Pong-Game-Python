from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.goto_up, "Up")
screen.onkey(r_paddle.goto_down, "Down")
screen.onkey(l_paddle.goto_up, "w")
screen.onkey(l_paddle.goto_down, "s")


score = Scoreboard()
is_game_on = True
while is_game_on:

    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #collision with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #collision with paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        #ball.bounce_y()
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
       # ball.bounce_y()
        ball.bounce_x()


    #ball missing the paddle
    if ball.xcor() >= 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() <= -380:
        ball.reset_position()
        score.r_point()
screen.exitonclick()
