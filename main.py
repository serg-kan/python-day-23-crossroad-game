import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Algorithm:
# 1. create a player turtle
# 1.1. give ability to move (move method + key binding)
# 2. create a car turtle
# 2.1. give ability to move (set position behind the right wall, move)

# How to manage cars? Should a car be a turtle in a separate class?
# Should CarManager return turtles in one of its methods?

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move()
