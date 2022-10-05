import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
level = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(fun=player.move, key='Up')

speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            level.game_over()

    if player.is_finish():
        player.reset_position()
        car_manager.level_up()
        level.level_up()


screen.exitonclick()