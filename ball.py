from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        """Ball served by left player at the beginning"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed = 5
        self.serve(game_level=1, x_=-469, y_=0)

    def serve(self, game_level, x_, y_):
        """Input serving paddle's location and current game level.
        Reset ball to correspondent location and speed.
        Set serving direction at a random angle(30-60 degree) to the serving paddle"""
        dirt_list = []
        if x_ < 0:
            for n in [1, 7]:
                dirt_list += list(range(n*45-15, n*45+15))
                self.goto(x_+11, y_)
        elif x_ > 0:
            for n in [3, 5]:
                dirt_list += list(range(n * 45 - 15, n * 45 + 15))
                self.goto(x_-11, y_)
        direction = random.choice(dirt_list)
        self.setheading(direction)
        self.speed = 4 + game_level

    def move(self):
        """Ball move at its current speed"""
        self.forward(self.speed)

    def bounce_wall(self):
        """bounce off the top or bottom wall"""
        current_direction = self.heading()
        self.setheading(360 - current_direction)

    def bounce_pad1(self):
        """bounce off the left paddle"""
        current_direction = self.heading()
        if 270 > current_direction > 180:
            self.setheading(540 - current_direction)
        if 180 > current_direction > 90:
            self.setheading(180 - current_direction)

    def bounce_pad2(self):
        """bounce off the right paddle"""
        current_direction = self.heading()
        if 360 > current_direction > 270:
            self.setheading(540 - current_direction)
        if 90 > current_direction > 0:
            self.setheading(180 - current_direction)
