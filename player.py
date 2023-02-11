from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def collison(self, lst):
        for car in lst:
            if self.distance(car) < 28:
                return True

    def is_finished(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def restart(self):
        self.goto(STARTING_POSITION)