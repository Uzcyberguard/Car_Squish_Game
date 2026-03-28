from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("car8.gif")
        self.penup()
        self.setheading(90)
        self.goto(0, -250)
