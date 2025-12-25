"""
Food module.

Defines the Food class, which represents an edible item
that the snake can consume to grow and increase score.

"""

from turtle import Turtle
import random

# Represents a food item in the Snake game. The food appears at random positions within the game boundaries and can be refreshed after being consumed.
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('white')
        self.speed(0)
        self.refresh()
        
    # Moves the food to a new random position within the game area.
    def refresh(self):
        xcor = random.randint(-350, 350)
        ycor = random.randint(-350, 350)
        self.goto(xcor, ycor)