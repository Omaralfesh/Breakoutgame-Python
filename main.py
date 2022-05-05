from turtle import Screen, Turtle
from ball import Ball
import time
from plates import Plates
screen = Screen()
screen.title("Breakout")
screen.setup(820, 800)
screen.bgcolor("black")
screen.tracer(0)


paddle = Turtle("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=7)
paddle.penup()
paddle.speed("fastest")
paddle.goto(x=0, y=-350)

ball = Ball()
plates = Plates()

def go_right():
    new_x = paddle.xcor() + 30
    paddle.goto(new_x, paddle.ycor())

def go_left():
    new_x = paddle.xcor() - 30
    paddle.goto(new_x, paddle.ycor())

screen.listen()
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

game_on = True
while game_on:
    time.sleep(0.04)

    screen.update()
    ball.move()
    for plate in plates.all_plates:
        if ball.ycor() >= plate.ycor() - 25 and plate.xcor() - 25 <= ball.xcor() <= plate.xcor() + 25:
            plate.hideturtle()
            plate.goto(-1000, -1000)
            ball.bounce_v()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_h()
    if ball.ycor() > 380:
        ball.bounce_v()
    if ball.ycor() < -380:
        ball.reset_position()
        ball.bounce_v()
    if ball.distance(paddle) < 50 and ball.ycor() < -330:
        ball.bounce_v()


screen.exitonclick()