from turtle import Turtle


class Board_line(Turtle):
    """Board line created with animation"""
    def __init__(self):
        super().__init__()
        self.shape = "square"
        self.hideturtle()
        # control instruction
        self.penup()
        self.pencolor("yellow")
        self.goto(0, 325)
        self.write(arg=f"\u2191  Q    \u2193  Z                                                                       "
                       f"                              \u2191  I    \u2193  M",
                   align="center", font=('Arial', 20, 'normal'))
        # logo
        self.pencolor("white")
        self.write(arg="Jay's pong game", align="center", font=('Arial', 30, 'normal'))
        # table line
        self.goto(0, -300)
        self.pensize(10)
        self.left(90)
        while self.ycor() <= 260:
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(30)
        self.penup()
        self.goto(-500, 300)
        self.pendown()
        self.setheading(0)
        for n in range(2):
            self.forward(1000)
            self.right(90)
            self.forward(600)
            self.right(90)
