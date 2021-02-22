from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        """initialisation of snake object"""
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_snake_seg = Turtle(shape='square')
        new_snake_seg.color("white")
        new_snake_seg.penup()
        new_snake_seg.goto(position)
        self.snake.append(new_snake_seg)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def extend(self):
        """add new segment to snake"""
        self.add_segment(self.snake[-1].position())

    def move_snake(self):
        for seg_nb in range(len(self.snake) - 1, 0, -1):
            # each snake's segment will take place of segment n-1 within snake
            # range function don't take in account seg 0 (stop before 0) : head
            new_x = self.snake[seg_nb - 1].xcor()
            new_y = self.snake[seg_nb - 1].ycor()
            self.snake[seg_nb].goto(new_x, new_y)

        # head impulse snake's movement
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        # if statement to avoid snake to go back on his self
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
