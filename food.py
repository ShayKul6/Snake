import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("cyan")
        self.speed("fastest")
        self.penup()
        self.new_location()

    def new_location(self):
        x_position = random.randint(-270, 270)
        y_position = random.randint(-270, 270)
        self.setpos(x_position, y_position)