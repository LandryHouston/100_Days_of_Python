# Draw a Dashed Line

import turtle as t

timmy = t.Turtle()
timmy.shape('turtle')
timmy.color('MediumPurple')
timmy.pensize(5)

for _ in range(10):
    timmy.forward(5)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen = t.Screen()
screen.exitonclick()