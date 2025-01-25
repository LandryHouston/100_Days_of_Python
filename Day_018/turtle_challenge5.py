# Draw a Spirograph

import turtle as t
import random

t.colormode(255)

timmy = t.Turtle()
timmy.shape('turtle')
timmy.pensize(2)
timmy.speed(0)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()