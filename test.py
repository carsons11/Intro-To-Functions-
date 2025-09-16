""" import turtle
from turtle import *
t = Turtle()
t.shape('turtle') """

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

""" def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)

def addsquare():
    y = 5
    for i in range(60):
        square(y)
        t.right(5)
        y=y+5
        t.speed(200)
addsquare()
turtle.done() """

""" #strings represent characters or text """
""" x = "Dang it Yi"
name = input("What's your name")
print(name)
def add(x,y):
    return x + y
z = add(5,15)
print(z) """

""" #integers of numbers
a = int('5')
bill = input("How much was the bill?")
print(int(bill) * .15) """

""" name = "Mason"
#use F string
print(f"His name is {name}")
 """

""" #Float
#bill = 3.14
students = ["Cadee", "Mason", "Andy"]
#Can reference each item in a list by their index
print(students[0]) #Prints Cadee

#add student
students.append("Alina") #append adds it into the list

#we can iterate or loop through a list
for student in students:
    print(student) """

""" #BooLean true or false
x = True
y = False
#for evaluations use double equal signs ==
if x == True:
    print("Hello Rodney") 
else:
    print("Goodbye Rodney") """

""" students = ["Cadee", "Mason", "Andy", "Alina"]
if "Alina" in students:
    print("She's here")
else:
    students.append("Alina")
    print("We added Alina")
 """
""" x = 91
if x <10:
    print("Less")
elif x == 10:
    print("Equal")
else:
    print("Greater than 10")

students = ["Cadee", "Mason", "Andy", "Alina"]
for student in students:
    found = False
    if student == "Mason":
        print("Found Mason")
        found = True """
""" name = "Cadee"
for letter in name:
    print(letter)"""  

import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed(999)
sidelength = 100
rotate = 144
def square(x,y):
    for i in range(5):
        t.forward(x)
        t.left(y)
def addSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 144)
        length += 5
        t.right(5)
addSquares(60)
turtle.done()