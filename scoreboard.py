from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.heading = "Pong Game"
        self.l_score = 0
        self.r_score = 0
        self.goto(0, 250)
        self.write(self.heading, align='center', font=("Courier", 40, 'normal'))
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=("Courier", 40, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=("Courier", 40, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.score_update()

    def r_point(self):
        self.r_score += 1
        self.score_update()
