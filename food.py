import random
from turtle import Turtle



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.9, stretch_len=0.9)
        self.color('pink')
        self.speed("fastest")
        self.random_location()

    def random_location(self) -> None:
        x = random.randint(-240, 240)
        y = random.randint(-240, 240)
        self.setposition(x, y)
