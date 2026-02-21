from PIL import Image
from turtle import Turtle, Screen
import os

screen = Screen()
screen.setup(width=800, height=600)

gif_files = [f"car{i}.gif" for i in range(1, 16)]
for pic in gif_files:
    screen.addshape(pic)








tim = Turtle()
tim.shape(gif_files[8])
tim.penup()


screen.exitonclick()