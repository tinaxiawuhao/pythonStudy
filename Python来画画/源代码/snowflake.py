# Python画雪花
# 公众号：Charles的皮卡丘
import turtle
from random import *


def ground():
    turtle.hideturtle()
    for i in range(400):
        turtle.pensize(randint(5, 10))
        x = randint(-400, 350)
        y = randint(-280, -1)
        r = -y/280
        g = -y/280
        b = -y/280
        turtle.pencolor(r, g, b)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(randint(40, 100))


def snow():
    turtle.hideturtle()
    turtle.pensize(2)
    for i in range(100):
        r = random()
        g = random()
        b = random()
        turtle.pencolor(r, g, b)
        turtle.penup()
        turtle.setx(randint(-350, 350))
        turtle.sety(randint(1, 270))
        turtle.pendown()
        dens = randint(8, 12)
        snowsize = randint(10, 14)
        for j in range(dens):
            turtle.forward(snowsize)
            turtle.backward(snowsize)
            turtle.right(360/dens)


def draw():
    turtle.setup(800, 600, 0, 0)
    # getscreen().tracer(30, 0)
    turtle.bgcolor("black")
    snow()
    ground()
    turtle.done()


if __name__ == '__main__':
    draw()