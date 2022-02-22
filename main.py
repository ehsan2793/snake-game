import random
import time
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
screen.listen()

colors = ['red', 'green', 'blue']
starting_position = [(0, 0), (-20, 0), (-40, 0)]
snake_parts = []

def move_forward():
    for i in snake_parts:
        i.forward(20)

# todo: erase the unwanted colors
# snake creation
i = 0
for position in starting_position:
    segment = Turtle('square')

    segment.color(colors[i])
    i+= 1
    segment.penup()
    segment.setposition(position)
    snake_parts.append(segment)


game_is_on = True
# snake move
while game_is_on:
    screen.update()
    for index in range( len(snake_parts)-1,0,-1):
        position=snake_parts[index - 1].position()
        snake_parts[index].setposition(position)
        time.sleep(0.2)
    snake_parts[0].forward(20)







screen.exitonclick()
