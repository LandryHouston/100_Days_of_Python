from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(25)

def move_backwards():
    timmy.backward(25)

def turn_cw():
    timmy.right(15)

def turn_ccw():
    timmy.left(15)
    
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_ccw)
screen.onkey(key='d', fun=turn_cw)
screen.onkey(key='c', fun=clear)
screen.exitonclick()