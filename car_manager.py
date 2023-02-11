from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []

    def create(self):
        chance = random.randint(1,6)
        if chance == 2 :
            new_car = Turtle(shape = "square")
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            ycor = random.randint(-240, 250)
            new_car.goto(290, ycor)
            self.cars.append(new_car)
        else:
            pass

    def moveCars(self, num):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT* num))



