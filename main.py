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
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True

scoreboard.print_level()
update = 0
while game_is_on:
    update += 1
    time.sleep(0.1)
    screen.update()

    # detect collision with upper wall
    if player.ycor() >= 300:
        scoreboard.update_level()
        scoreboard.print_level()
        player.reset()
        car_manager.update_level()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.print_game_over()
            game_is_on = False



screen.exitonclick()