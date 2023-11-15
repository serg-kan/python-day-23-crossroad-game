from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1, 6)

        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)

            y_position = random.randint(-250, 250)
            car.goto(x=310, y=y_position)

            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.goto(x=car.xcor() - self.move_distance, y=car.ycor())

        # if self.xcor() < -320:
        #     x_position = random.randint(300, 500)
        #     y_position = random.randint(-250, 280)
        #     self.goto(x=x_position, y=y_position)

    def update_level(self):
        self.move_distance += MOVE_INCREMENT



