"""
Module: draw_pentagon

Program to draw a pentagon using turtles.
"""

import turtle

# create a turtle and set the pen color
sat = turtle.Turtle()
sat.pencolor(input("What pen color?"))

sun = turtle.Turtle()
sun.pencolor("green")


# draw the pentagon
sat.forward(150)
sat.left(72)
sat.forward(150)
sat.left(72)
sat.forward(150)
sat.left(72)
sat.forward(150)
sat.left(72)
sat.forward(150)
sat.left(72)

#draw smaller pentagon
sun.up()
sun.goto(5,5) #move smaller pentagon so lines dont overlap
sun.down()
sun.forward(25)
sun.left(72)
sun.forward(25)
sun.left(72)
sun.forward(25)
sun.left(72)
sun.forward(25)
sun.left(72)
sun.forward(25)
# keep the turtle window open until we click on it
turtle_window = turtle.Screen()
turtle_window.exitonclick()