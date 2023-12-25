
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("PONG PONG")
screen.tracer(0)


r_paddle= Paddle((370, 0))
l_paddle= Paddle((-370, 0))
ball =  Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#ball bounces with wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

#ball collided with paddles and bouncing back 
    if ball.distance(r_paddle) < 50 and ball.xcor() > 360 or ball.distance(l_paddle) < 50 and ball.xcor() > -360:
        ball.bounce_x()

# r_paddle misses:
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

# l_paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    


screen.exitonclick()