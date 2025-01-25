# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 12)
# for color in colors:
#     new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [
    (183, 7, 46),
    (215, 222, 235),
    (159, 96, 30),
    (23, 95, 185),
    (235, 243, 239),
    (193, 157, 91),
    (246, 216, 52),
    (218, 145, 175),
    (178, 201, 6),
    (246, 235, 241),
    (67, 154, 95),
]


import turtle as t
import random

t.colormode(255)

timmy = t.Turtle()
timmy.speed(0)
timmy.hideturtle()
timmy.up()

timmy.setheading(220)
timmy.forward(640)
timmy.setheading(0)

for i in range(10):
    for _ in range(10):
        timmy.dot(50, random.choice(color_list))
        timmy.forward(100)
    timmy.setheading(90)
    timmy.forward(100)
    timmy.setheading(180)
    timmy.forward(1000)
    timmy.setheading(360)


screen = t.Screen()
screen.exitonclick()