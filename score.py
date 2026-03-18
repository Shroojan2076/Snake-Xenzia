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

        self.title = Turtle()
        self.title.hideturtle()
        self.title.penup()
        self.title.color("white")

        self.write_title()

        self.partition = Turtle()
        self.partition.goto(0, 340)
        self.partition.hideturtle()
        self.partition.penup()
        self.partition.shape("square")
        self.partition.shapesize(0.2, 50)
        self.partition.fillcolor("YellowGreen")
        self.partition.showturtle()

        self.pause = Turtle()
        self.pause.hideturtle()
        self.pause.penup()
        self.pause.color("white")

        self.gameover = Turtle()
        self.gameover.hideturtle()
        self.gameover.penup()
        self.gameover.color("white")

    def write_title(self):
        self.title.goto(-280, head[1])
        self.title.write("Snake Xenzia", align='center', font=("Trebuchet MS", 24, 'bold'))

    # Updates the scoreboard after each successful food eatiing.  
    def update(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)
    
    # Displays the game-over message at the center top of the screen.
    def game_over(self):
        self.gameover.goto(0, 0)
        self.gameover.write('Game Over', align=ALIGNMENT, font=FONT)

    def hide_game_over(self):
        self.gameover.clear()

    # Increments the score by one and updates the on-screen display.
    def inc_score(self):
        self.score += 1
        self.clear()
        self.update()

    def reset_score(self):
        self.score = 0
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def paused(self):
        self.pause.goto(0, 0)
        self.pause.write("Paused", align="center", font=("Arial", 20, "bold"))

    def hide_pause(self):
        self.pause.clear()