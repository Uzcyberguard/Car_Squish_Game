import turtle

class Road2():
    def __init__(self):

            self.screen = turtle.Screen()
            self.tim3 = turtle.Turtle()
            self.tim4= turtle.Turtle()

            self.screen.tracer(0)
            self.tim3.penup()
            self.tim4.penup()
            self.tim3.shape("road.gif")
            self.tim4.shape("road.gif")
            self.tim3.setheading(-90)
            self.tim4.setheading(-90)
            self.tim4.goto(0,640)
            self.screen.update()
    def move(self):
         self.screen.tracer(0)

         self.tim3.forward(8)
         self.tim4.forward(8)

         if self.tim3.ycor()<=-640:
             self.tim3.goto(0,640)
         if self.tim4.ycor()<=-640:
             self.tim4.goto(0,640)

         self.screen.update()

