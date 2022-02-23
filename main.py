import random
import time
from turtle import Screen
from snake import Snake
from food import Food
screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
screen.listen()




snake = Snake()
food =Food()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')
screen.onkey(snake.change_color,'c')
game_is_on = True

# snake move
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) <= 15:
        food.random_location()



screen.exitonclick()
