"""
Module: draw_pentagon

Program to draw a pentagon using turtles.
"""

import turtle

# create a turtle and set the pen color
sat = turtle.Turtle()
sat.pencolor("red")

for item in range(6):
    sat.forward(50)
    sat.left(72)
# draw the pentagon

# keep the turtle window open until we click on it
turtle_window = turtle.Screen()
turtle_window.exitonclick()