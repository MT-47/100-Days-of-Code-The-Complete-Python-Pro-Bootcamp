#####Turtle Intro######
from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")

########### Challenge 3 - Draw Shapes ########


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]

for num_sides in range(3, 10):
    tim.color(random.choice(colours))
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(360 / num_sides)

screen = Screen()
screen.exitonclick()
