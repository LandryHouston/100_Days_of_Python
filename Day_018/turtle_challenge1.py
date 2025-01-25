# Draw a Square

import turtle as t

timmy = t.Turtle()
timmy.shape('turtle')
timmy.color('MediumPurple')
timmy.pensize(5)

timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)

screen = t.Screen()
screen.exitonclick()