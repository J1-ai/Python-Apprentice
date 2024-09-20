
"""
Turtles with a loop. 

This program has four identical lines of code to draw a square, 
but you know you can use a loop to make the program simpler. 

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
window=turtle.Screen()
window.bgcolor('red')
tina = turtle.Turtle()                  # Create a turtle named tina
for i in range (4):
    tina.forward (15)
    tina.left (90)                # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 
for i in range (4):
    tina.forward(30)                       # Move tina forward by the forward distance
    tina.left(90)                           # Turn tina left by the left turn

for i in range (4):
    tina.forward (45)
    tina.left (90)

for i in range (4):
    tina.forward (60)
    tina.left (90)

for i in range (4):
    tina.forward (75)
    tina.left (90)

for i in range (4):
    tina.forward (90)
    tina.left (90)

for i in range (4):
    tina.forward (105)
    tina.left (90)

for i in range (4):
    tina.forward (120)
    tina.left (90)

for i in range (4):
    tina.forward (135)
    tina.left (90)










turtle.exitonclick()                    # Close the window when we click on it
