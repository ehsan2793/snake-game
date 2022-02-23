import random
from turtle import Turtle
import time

STRING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]
        self.head.color('orange')

    def create_snake(self):
        for position in STRING_POSITION:
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.setposition(position)
            self.snake_parts.append(segment)

    def move(self):
        for index in range(len(self.snake_parts) - 1, 0, -1):
            position = self.snake_parts[index - 1].position()
            self.snake_parts[index].setposition(position)
        self.head.forward(DISTANCE)

    def add_to_tail(self):
        pass


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def change_color(self):
        r =random.randint(0,255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.head.color((r,g,b))

    def position(self):
        return self.head.position()