import random
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard

screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
screen.listen()

score = ScoreBoard()

snake = Snake()

food = Food()
food1 = Food()
food2 = Food()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.change_color, 'c')
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collisions with food
    if snake.head.distance(food) <= 15:
        food.random_location()
        snake.extend_snake()
        score.add_to_score()
    if snake.head.distance(food1) <= 15:
        food1.random_location()
        snake.extend_snake()
        score.add_to_score()
    if snake.head.distance(food2) <= 15:
        food2.random_location()
        snake.extend_snake()
        score.add_to_score()
    # Detect collisions with wall
    if (snake.head.xcor() > 285
            or snake.head.xcor() < -299
            or snake.head.ycor() < -280
            or snake.head.ycor() > 299):
        score.reset_scoreBoard()
        snake.reset_snake()

    for segment in snake.snake_parts[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_scoreBoard()
            snake.reset_snake()

screen.exitonclick()
