"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Turtle Image"


Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
window=turtle.Screen()

tina = turtle.Turtle() 
j=tina
j.shape('turtle')
window=turtle.Screen()                 # Create a turtle named tina
window.bgcolor('yellow')
j.color ('blue')
j.pencolor ('blue')
# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()
j.speed (8)
j.pendown ()
j.begin_fill()
j.forward (150)
j.left(90)
j.forward(60)
j.right(90)
j.forward(60)
j.left(-90)
j.forward(120)
j.right(90)
j.forward(210)
j.right(90)
j.forward(60)
j.end_fill()
tina.penup()
j.goto(0,40)








j.penup()
j.pendown()
j.pendown ()
j.begin_fill()
j.forward (150)
j.right(90)
j.forward(60)
j.left(90)
j.forward(60)
j.right(-90)
j.forward(120)
j.left(90)
j.forward(210)
j.left(90)
j.forward(60)
j.end_fill()
tina.penup()
j.speed(1)
tina.goto(45,-115)
j.left(180)
j.pendown()
j.forward(80)
j.right(90)
j.forward(130)
j.right(360)
j.right(90)
j.forward(120)
j.right(360)
j.left(90)
j.forward(120)
j.right(90)
j.forward(50)
j.speed(3)
j.right(720)
j.write('        Yay!')


















































turtle.exitonclick()