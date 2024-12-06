"""

Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help

"""

import random

import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=700)    # Set the size of the window

tina = turtle.Turtle()



def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))
                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(200)

def getNextColor(i):
    return colors[i % len(colors)]
                           # Make the turtle move as fast, but not too fast. 
tina.speed(4)


forwards = [ 50 ]
lefts = [ 90 ]
colors = [  'getRandomColor' ]

for  i in range(4):

    forward = 50
    left = 90
    color = "getRandomColor"


    tina.pencolor("getRandomColor")
    tina.forward(50)
    tina.left(90)

turtle.exitonclick()  

