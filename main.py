"""
Main entry point for the Snake Xenzia game.

Initializes game objects, handles the main game loop,
processes user input, and coordinates interactions
between snake, food, and score modules.
"""

from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Score

screen_height = 800
screen_width = 800
snake_len = 3
game_on = False

scr = Screen()
scr. bgcolor('black')
scr.title('Snake Xenzia')
scr.setup(width= screen_width, height= screen_height)
scr.tracer(0)

snake = Snake()
food = Food()
score = Score()

scr.listen()
scr.onkey(snake.up, 'Up')
scr.onkey(snake.down, 'Down')
scr.onkey(snake.left, 'Left')
scr.onkey(snake.right, 'Right')


game_on = True
while game_on:
    scr.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) <= 15:
        food.refresh()
        score.inc_score()
        snake.extend()
    
    if snake.head.xcor() <= -395 or snake.head.xcor() >= 395 or snake.head.ycor() <= -395 or snake.head.ycor() >= 395:
        game_on = False
        score.game_over()
    
    for block in snake.blocks[1:]:
        if snake.head.distance(block) <= 10:
            game_on = False
            score.game_over()

scr.exitonclick()





































