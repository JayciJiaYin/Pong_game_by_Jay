from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 24, 'normal')
COLOR = "white"


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.score1 = 0
        self.score2 = 0
        self.goal = 5
        self.hideturtle()
        self.penup()
        self.color(COLOR)
        self.goto(0, 262)
        self.refresh()

    def refresh(self):
        """"Refresh scoreboard"""
        self.clear()
        self.write(arg=f"{self.score1}/{self.goal}          Level: {self.level}          {self.score2}/{self.goal}",
                   align=ALIGN, font=FONT)

    def level_up(self):
        """check current game status. level up the game if it is needed. Return False if game over"""
        if self.score1 >= 4 or self.score2 >= 4:
            if (self.score1 - self.score2) ** 2 >= 4 and (self.score1 >= 5 or self.score2 >= 5):
                return self.game_over()
            elif self.score1 - self.score2 == 0:
                self.level += 1
                self.goal += 1
                self.refresh()
        return True

    def score_up(self, player):
        """Increase the score for input player"""
        if player == 1:
            self.score1 += 1
        elif player == 2:
            self.score2 += 1
        self.refresh()

    def game_over(self):
        """Return False and output the winner"""
        self.refresh()
        winner = "Winner!"
        if self.score1 > self.score2:
            self.goto(-250, 0)
            self.write(arg=winner, align=ALIGN, font=FONT)
        else:
            winner = "Winner!"
            self.goto(250, 0)
            self.write(arg=winner, align=ALIGN, font=FONT)
        return False

