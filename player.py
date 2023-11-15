from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("turtle")
        self.goto(x=0, y=-280)
        self.setheading(90)

    def move(self):
        self.forward(20)

    def reset(self):
        self.goto(x=0, y=-280)
