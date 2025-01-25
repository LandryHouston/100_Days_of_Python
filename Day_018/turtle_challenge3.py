# Drawing Different Shapes

import turtle as t
import random

timmy = t.Turtle()
timmy.shape('turtle')
timmy.pensize('5')

colors = ['coral', 'CornflowerBlue', 'DarkSeaGreen', 'IndianRed', 'LightSalmon', 'MediumPurple', 'PaleGreen', 'plum', 'tomato', 'SlateBlue', 'thistle']

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for i in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(i)

screen = t.Screen()
screen.exitonclick()