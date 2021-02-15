from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

screen.title("Snake Game")

snake = Snake()
screen.tracer(0)

game_is_on = True
while game_is_on:
    # refresh screen:
    screen.update()
    # every 0.2 sec
    time.sleep(0.2)

    snake.move_snake()


screen.exitonclick()
