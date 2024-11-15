import turtle
j=turtle.Turtle()


def set_turtle_image(turtle, image_name):
    from pathlib import Path
    image_dir=Path(__file__).parent/"images"
    image_path=str(image_dir/image_name)

    screen=turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

screen=turtle.Screen()
screen.setup(width=600, height=600)

set_turtle_image(j, "snake.gif")
j.penup()
j.speed(2)

for i in range(2):
    j.goto(100,100)
    j.goto(-100,-100)

set_turtle_image(j, "badger.gif")

for i in range(3):
    j.goto(-100,-100)
    j.goto(100,100)

set_turtle_image(j, "mushroom.gif")

for i in range(2):
    j.goto(100,100)
    j.goto(-100,-100)


j.penup()

turtle.exitonclick()




