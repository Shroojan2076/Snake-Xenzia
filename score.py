"""
Score module.

Provides a Score class for displaying and updating
the player's score during the Snake game.

"""

from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 18, 'bold')
head = (0, 350)

# Manages score display and game-over messaging. Uses turtle graphics to render text on the screen.
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(head)
        self.hideturtle()
        self.update()
        
    # Updates the scoreboard after each successful food eatiing.  
    def update(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
    
    # Displays the game-over message at the center top of the screen.
    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align=ALIGNMENT, font=FONT)

    # Increments the score by one and updates the on-screen display.
    def inc_score(self):
        self.score += 1
        self.clear()
        self.update()
    