"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

tina.shape ('triangle')

tina.forward
tina.pencolor ('purple')
tina.left (9)
tina.forward (16)
tina.right (18)
tina.forward (36)
tina.penup
tina.pendown
tina.color ('orange')
tina.begin_fill ()
tina.circle (40)
tina.end_fill ()
tina.left (90)
tina.forward (120)
tina.left (75)
tina.forward (100)
tina.color ('black')
tina.begin_fill ()
tina.circle (40)
tina.end_fill ()
tina.left (60)
tina.forward (150)
tina.color ('blue')
tina.begin_fill ()
tina.circle (40)
tina.end_fill ()











turtle.exitonclick()                    # Close the window when we click on it
