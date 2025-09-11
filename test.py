import turtle
from turtle import *
t = Turtle()
t.shape('turtle')

""" def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)

for i in range(100):
    square(200)
    t.right(5)
    t.speed(200) """


""" sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
def addSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length += 25
addSquares(5) """

def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)

for i in range(60):
    square(5)
    t.speed(200)
sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
def addSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 90)
        length += 5
        t.left(5)
addSquares(5)
