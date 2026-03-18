from turtle import Turtle

class Button(Turtle):
    def __init__(self, text, position, action):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.action = action
        self.text = text

        self.shape("square")
        self.shapesize(1, 3)
        self.fillcolor("YellowGreen")
        self.showturtle()

        self.label = Turtle()
        self.label.hideturtle()
        self.label.penup()
        self.label.color("white")
        self.label.goto(position[0], position[1] + 10)
        self.label.write(self.text, align="center", font=("Arial", 12, 'bold'))

        self.onclick(self.clicked)

    def set_text(self, new_text):
        self.text = new_text
        self.label.clear()
        self.label.write(self.text, align="center", font=("Arial", 12, 'bold'))

    def clicked(self, x, y):
        self.action()

class Menu():
    def __init__(self, play_pause, quit, restart):
        self.play_pause_btn = Button("Pause", (200, 360), play_pause)
        self.quit_btn = Button("Quit", (270, 360), quit)
        self.restart_btn = Button("Restart", (340, 360), restart)