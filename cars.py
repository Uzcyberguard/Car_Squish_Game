import random
from turtle import Turtle, Screen
class Cars:
    def __init__(self,gifs):

        self.gifs = gifs
        self.moving_cars = []
        self.initial_positions = [-240,-200,-160,-120,-80,-40,0,40,80,120,160,200,240]



    def create_rand_cars(self):
        for _ in range(7):
             new_car = Turtle()
             new_car.penup()
             new_car.shape(random.choice(self.gifs))
             self.moving_cars.append(new_car)
        positions = random.sample(self.initial_positions,7)
        i = 0

        for car in self.moving_cars[-7::]:

            car.goto(positions[i],random.randint(400,700))
            car.setheading(-90)
            i+=1
