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
tina.speed (1)

tina.shape ('turtle')

tina.color ('green')
tina.left (2880)
tina.forward
tina.pencolor ('black')
tina.begin_fill ()
tina.circle (105)
tina.end_fill ()
tina.penup ()
tina.goto (-50,100)
tina.pendown ()
tina.color ('white')
tina.pencolor ('white')
tina.begin_fill ()
tina.circle (20)
tina.end_fill ()
tina.color ('red')
tina.begin_fill ()
tina.circle (10)
tina.end_fill ()
tina.penup ()
tina.goto (50,100)
tina.pendown ()
tina.color ('white')
tina.pencolor ('white')
tina.begin_fill ()
tina.circle (20)
tina.end_fill ()
tina.color ('red')
tina.begin_fill ()
tina.circle (10)
tina.end_fill ()
tina.pencolor ('red')
tina.color  ('red')
tina.penup ()
tina.goto (-40,10)
tina.pendown ()
tina.begin_fill ()
tina.forward (75)
tina.left (45)
tina.left (45)
tina.forward (75)
tina.left (45)
tina.left (45)
tina.forward (75)
tina.left (45)
tina.left (45)
tina.forward (75)
tina.end_fill ()
tina.penup ()
tina.goto (25,0)
tina.pendown ()
tina.begin_fill ()
tina.color ('green')
tina.pencolor ('green')
tina.forward (45)
tina.left (90)
tina.forward (-50)
tina.left (90)
tina.forward (45)
tina.right (90)
tina.forward (50)
tina.end_fill ()
tina.penup ()
tina.goto (55,-40)
tina.pendown ()
tina.begin_fill ()
tina.right (90)
tina.forward (100)
tina.left (-90)
tina.forward (110)
tina.left (-90)
tina.forward (100)
tina.right (90)
tina.forward (110)
tina.end_fill ()
tina.penup ()
tina.goto (-140,-90)
tina.pendown ()
tina.begin_fill ()
tina.forward (300)
tina.left (90)
tina.forward (25)
tina.left (90)
tina.forward (300)
tina.left (90)
tina.forward (25)
tina.end_fill ()
















tina.penup ()
tina.goto (0,-500)












































turtle.exitonclick()                    # Close the window when we click on it
