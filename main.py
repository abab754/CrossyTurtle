import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
screen.listen()
screen.onkey(fun=player.move, key="Up")

cm = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cm.create()
    cm.moveCars(scoreboard.level)

    if player.collison(cm.cars):
        scoreboard.game_over()
        game_is_on = False

    if player.is_finished():
        scoreboard.update()
        player.restart()





screen.exitonclick()
