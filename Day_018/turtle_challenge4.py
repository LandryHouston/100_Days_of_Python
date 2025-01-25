import turtle as t
import random

t.colormode(255)

timmy = t.Turtle()
timmy.shape('turtle')
timmy.pensize(15)
timmy.speed(0)

directions = [0, 90, 180, 270]

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def random_walk():
    timmy.forward(20)
    timmy.setheading(random.choice(directions))

for _ in range(250):
    timmy.color(random_color())
    random_walk()

screen = t.Screen()
screen.exitonclick()