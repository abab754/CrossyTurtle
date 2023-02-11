from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.highscore = 0
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.write(arg=f"Level: {self.level + 1}", font= FONT)

    def update(self):
        self.clear()
        self.level += 1
        self.goto(-260, 260)
        self.write(arg=f"Level: {self.level + 1}", font= FONT)


    def game_over(self):
        self.clear()
        self.home()
        self.write(arg="Game Over", font= FONT)




