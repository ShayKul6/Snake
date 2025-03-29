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
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.turn_left, "a")
screen.onkey(snake.turn_right, "d")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:  # if distance between objects less than 15, generate new location
        food.new_location()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if (snake.head.xcor() > 280 or snake.head.ycor() > 260
            or snake.head.xcor() < -290 or snake.head.ycor() < -280):
        game_on = False
        scoreboard.end_game()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.end_game()

screen.exitonclick()