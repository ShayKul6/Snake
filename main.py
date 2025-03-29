import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # stops automatic updates

snake = Snake()  # creates a snake
food = Food()  # creates a circle 'food'
scoreboard = Scoreboard()  # creates a scoreboard object

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:  # if distance between objects less than 15, generate new location
        food.new_location()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()

    # Detect collision with wall


    # Detect collision with tail
screen.exitonclick()