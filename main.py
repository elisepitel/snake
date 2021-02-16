from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

# link user key input to snake movement
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
score = 0

while game_is_on:
    # refresh screen:
    screen.update()
    # every 0.1 sec
    time.sleep(0.1)

    snake.move_snake()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.update_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        score_board.game_over()

    # Detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()


screen.exitonclick()
