from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=2)

        y_position = random.randint(-250, 280)
        self.goto(x=0, y=y_position)

    def init_cars(self):
        cars = []

        for i in range(0, 10):
            x_position = random.randint(300, 400)
            y_position = random.randint(-250, 280)




    def move(self):
        self.goto(x=self.xcor() - STARTING_MOVE_DISTANCE, y=self.ycor())
