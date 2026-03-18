"""
Main entry point for the Snake Xenzia game.

Initializes game objects, handles the main game loop,
processes user input, and coordinates interactions
between snake, food, and score modules.
"""

from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
from menu import Menu

screen_height = 800
screen_width = 800
snake_len = 3
game_on = False
game_state = "running"

scr = Screen()
scr. bgcolor('black')
scr.title('Snake Xenzia')
scr.setup(width= screen_width, height= screen_height)
scr.tracer(0)

def play_pause_game():
    global game_state
    if game_state == 'running':
        game_state = 'paused'
        score.paused()
        menu.play_pause_btn.set_text("Resume")
    elif game_state == 'paused':
        game_state = 'running'
        score.hide_pause()
        menu.play_pause_btn.set_text("Pause")

def quit_game():
    global game_on
    game_on = False
    scr.bye()

def restart_game():
    global game_state, game_on
    game_state = 'running'
    game_on = True
    score.reset_score()
    food.refresh()
    snake.reset_position()
    score.hide_pause()
    score.hide_game_over()
    menu.play_pause_btn.set_text("Pause")

menu = Menu(play_pause_game, quit_game, restart_game)
    

snake = Snake()
food = Food()
score = Score()

scr.listen()
scr.onkey(snake.up, 'Up')
scr.onkey(snake.down, 'Down')
scr.onkey(snake.left, 'Left')
scr.onkey(snake.right, 'Right')


game_on = True
try:
    while game_on:
        scr.update()
        if game_state == "running":
            time.sleep(max(0.05, 0.1 - len(snake.blocks)*0.002))
            snake.move()

            if snake.head.distance(food) <= 15:
                food.refresh()
                score.inc_score()
                snake.extend()
        
            if snake.collision(screen_width, screen_height):
                game_state = 'over'
                score.game_over()

            if snake.self_collision():
                game_state = 'over'
                score.game_over()

except Exception as e:
    print(e)
    print('Game Closed.')

scr.mainloop()




































