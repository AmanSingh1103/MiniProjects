from turtle import Turtle , Screen

timmy = Turtle()
screen = Screen()


def move_forwards():
    timmy.forward(10)
def move_backward():
    timmy.backward(10)
def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)
def turn_left():
    timmy.left(10)
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.exitonclick()
