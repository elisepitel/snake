from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        """initialisation of snake object"""
        self.snake = []
        self.create_snake()

    def create_snake(self):

        for position in STARTING_POSITIONS:
            new_snake_seg = Turtle(shape='square')
            new_snake_seg.color("white")
            new_snake_seg.penup()
            new_snake_seg.goto(position)
            self.snake.append(new_snake_seg)

    def move_snake(self):

        for seg_nb in range(len(self.snake) - 1, 0, -1):
            # range function don't take in account seg 0 (stop before 0)
            new_x = self.snake[seg_nb - 1].xcor()
            new_y = self.snake[seg_nb - 1].ycor()
            self.snake[seg_nb].goto(new_x, new_y)

        self.snake[0].forward(MOVE_DISTANCE)
