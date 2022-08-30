from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Board
from boardline import Board_line
import time
# creat screen
screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("Jay's Pong Game")
screen.tracer(0)
# creat objects with animation
score_board = Board()
screen.tracer(1)
paddle = Paddle()
ball = Ball()
board_line = Board_line()

# paddle controls
screen.listen()
screen.onkey(paddle.p1up, "q")
screen.onkey(paddle.p1down, "z")
screen.onkey(paddle.p2up, "i")
screen.onkey(paddle.p2down, "m")

# game on
game_on = True
screen.tracer(0)
while game_on:
    # 142fps
    screen.update()
    time.sleep(0.007)
    ball.move()
    # wall bounce detection
    if (int(ball.ycor()) >= 290) or (int(ball.ycor()) <= -290):
        ball.bounce_wall()

    # paddle bounce detection and increase ball speed for every paddle bounce
    if (int(ball.xcor()) <= -460) and int(ball.distance(paddle.p1)) <= 53:
        ball.speed += 1
        ball.bounce_pad1()

    if (int(ball.xcor()) >= 460) and int(ball.distance(paddle.p2)) <= 53:
        ball.speed += 1
        ball.bounce_pad2()

    # misses detection and the player who gained poit will serve the ball
    # Checking and update the game status
    if int(ball.xcor()) <= -500:
        score_board.score_up(player=2)
        game_on = score_board.level_up()
        ball.serve(game_level=score_board.level, x_=paddle.p2.xcor(), y_=paddle.p2.ycor())

    if int(ball.xcor()) >= 500:
        score_board.score_up(player=1)
        game_on = score_board.level_up()
        ball.serve(game_level=score_board.level, x_=paddle.p1.xcor(), y_=paddle.p1.ycor())

# click screen to manually end the game
screen.exitonclick()
