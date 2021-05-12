##Square
import turtle
t = turtle.Turtle()

t.speed(0)

def square(x):
    for _ in range(3):
        t.fd(x)
        t.rt(120)
for _ in range (12):
    square(100)
    t.rt(30)

##Star
import random
def star(x, y, l, n):
    t.penup()
    t.goto(x, y)
    # t.setheading(random.randint(0,359))
    t.pendown()
    for _ in range(n):
        t.fd(l)
        t.bk(l)
        t.rt(360/n)

t.pensize(20)
star(0, 0, 200, 7)
t.pensize(15)
t.color(0.25, 0.25, 0.25)
star(0, 0, 200, 7)
t.pensize(10)
t.color(0.5, 0.5, 0.5)
star(0, 0, 200, 7)
t.pensize(5)
t.color(0.75, 0.75, 0.75)
star(0, 0, 200, 7)
t.pensize(2)
t.color(1, 1, 1)
star(0, 0, 200, 7)
t.hideturtle
input("Press any key to exit ...")