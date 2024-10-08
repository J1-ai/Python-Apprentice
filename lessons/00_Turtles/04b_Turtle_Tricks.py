"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina
j=tina
# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()


... # Your code here
window=turtle.Screen()
window.bgcolor('blue')
j.pencolor ('white')
j.color ('green')
j.begin_fill ()
for i in range (12):
    j.forward (200)
    j.left (150)
j.end_fill ()

turtle.exitonclick()                    # Close the window when we click on it