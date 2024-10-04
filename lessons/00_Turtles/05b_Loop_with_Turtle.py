
"""
Turtles with a loop. 

This program has four identical lines of code to draw a square, 
but you know you can use a loop to make the program simpler. 

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
window=turtle.Screen()
window.bgcolor('blue')
tina = turtle.Turtle() 
distance=15 
count=1
tina.pencolor ('blue')
tina.color('red')
tina.begin_fill()                # Create a turtle named tina
for i in range (248):
    tina.forward (distance)
    tina.right (90) 
    # distance+=15 
    count+=1 
    if count %4 == 0:
        distance+=5
tina.end_fill()             # Set the shape of the turtle to a turtle
tina.speed(0)                           # Make the turtle move as fast, but not too fast. 
# for i in range (4):
#     tina.forward(30)                       # Move tina forward by the forward distance
#     tina.left(90)                           # Turn tina left by the left turn

# for i in range (4):
#     tina.forward (45)
#     tina.left (90)

# for i in range (4):
#     tina.forward (60)
#     tina.left (90)

# for i in range (4):
#     tina.forward (75)
#     tina.left (90)

# for i in range (4):
#     tina.forward (90)
#     tina.left (90)

# for i in range (4):
#     tina.forward (105)
#     tina.left (90)

# for i in range (4):
#     tina.forward (120)
#     tina.left (90)

# for i in range (4):
#     tina.forward (135)
#     tina.left (90)

# for i in range (4):
#     tina.forward (150)
#     tina.left (90)

# for i in range (4):
#     tina.forward (165)
#     tina.left (90)

# for i in range (4):
#     tina.forward (180)
#     tina.left (90)

# for i in range (4):
#     tina.forward (195)
#     tina.left (90)

# for i in range (4):
#     tina.forward(210)
#     tina.left(90)

# for i in range (4):
#     tina.forward (225)
#     tina.left (90)

# for i in range (4):
#     tina.forward (240)
#     tina.left(90)








































turtle.exitonclick()                    # Close the window when we click on it
