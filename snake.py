'''
Snake module.

Defines the Snake class, which manages snake body segments,
movement logic, growth behavior, and direction control for
a classic Snake game implemented using turtle graphics.

'''

from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
      
    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]
        self.head.setheading(0)

    # Generates the one block whichh is to be added at the end of the snake
    def add_block(self, position):
        snake = Turtle('square')
        snake.color('YellowGreen')
        snake.penup()
        snake.goto(position)
        self.blocks.append(snake)

    # Creates the inital 3 - block snake.
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_block(position)
    
    # Moves the snake forward by one step.
    def move(self):
        for part in range(len(self.blocks)-1, 0, -1):
            pos = self.blocks[part - 1].pos()
            self.blocks[part].goto(pos)
        self.head.forward(MOVE_DISTANCE)

    # Extends the snake by adding a new segment at the tail.
    def extend(self):
        self.add_block(self.blocks[-1].position())

    # Changes the snake's heading to upward direction if the snake is currently not moving downward.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Changes the snake's heading to downward direction if the snake is currently not moving upward.
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Changes the snake's heading to left direction if the snake is currently not moving right-ward.
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Changes the snake's heading to right direction if the snake is currently not moving left-ward.
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_position(self):
        for block in self.blocks:
            block.hideturtle()
        self.blocks.clear()
        self.create_snake()
        self.head = self.blocks[0]
        self.head.setheading(0)
        self.move()

    def collision(self, width, height):
        if self.head.xcor() <= -(width/2 - 5) or self.head.xcor() >= (width/2 - 5) or self.head.ycor() <= -(height/2 - 5) or self.head.ycor() >= (height/2 - 80):
            return True
        return False
        
    def self_collision(self):
        for block in self.blocks[1:]:
                if self.head.distance(block) <= 10:
                    return True
        return False
