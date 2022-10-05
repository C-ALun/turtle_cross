FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.goto(-260, 240)
        self.penup()
        self.hideturtle()
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f'Level: {self.level}', font=FONT)

    def level_up(self):
        self.level += 1
        self.update_board()

    def game_over(self):
        self.goto(-70, 20)
        self.write('GAME OVER', font=FONT)