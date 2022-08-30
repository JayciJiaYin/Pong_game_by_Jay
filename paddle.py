from turtle import Turtle


class Paddle:

    def __init__(self):
        self.paddles = []
        self.create()
        self.p1 = self.paddles[0]
        self.p2 = self.paddles[1]

    def create(self):
        """ create two paddle objects which contained in a list called 'paddles' """
        for n in [-1, 1]:
            pad = Turtle(shape="square")
            pad.penup()
            pad.color("white")
            pad.shapesize(stretch_len=4, stretch_wid=1)
            pad.left(90)
            pad.goto(n*480, 0)
            self.paddles.append(pad)

    def p1up(self):
        """left paddle move up"""
        if self.p1.ycor() < 240:
            self.p1.forward(42)

    def p1down(self):
        """left paddle move down"""
        if self.p1.ycor() > -240:
            self.p1.forward(-42)

    def p2up(self):
        """right paddle move up"""
        if self.p2.ycor() < 240:
            self.p2.forward(42)

    def p2down(self):
        """right paddle move down"""
        if self.p2.ycor() > -240:
            self.p2.forward(-42)
