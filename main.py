from PIL import Image
from turtle import Turtle, Screen
import os

from PIL.ImageOps import expand

screen = Screen()
screen.setup(width=800, height=700)
screen.bgcolor("gray25")
gif_files = [f"car{i}.gif" for i in range(1, 16)]
for pic in gif_files:

    screen.addshape(pic)








tim = Turtle()
tim.shape(gif_files[8])
tim.penup()
tim.setheading(90)
tim.goto(0,-300)
tim2 = Turtle()
tim2.shape(gif_files[10])
screen.exitonclick()