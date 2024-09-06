"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle 
import random                          # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

tina.forward(100)
tina.left(100)
tina.pencolor("blue")

... # Your code here

def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["blue", "blue", "blue", "blue", "blue"]

def getNextColor(i):
    return colors[i % len(colors)]

window = turtle.Screen()

baseSize = 150  # the size of the black part of the star
flameSize = 80  # the length of the flaming arms

t = turtle.Turtle()
t.shape("turtle")
t.width(2) 
t.speed(0)  


for i in range(25):

    t.pencolor(getRandomColor())
    t.fillcolor(getRandomColor())  

    t.begin_fill()

    t.right(360 / 8) 
    t.forward(64)

    t.left(40) 

    t.forward(flameSize)
    t.right(170) 
    t.forward(flameSize)
    t.right(62) 
    t.forward(baseSize) 

    t.end_fill()

t.hideturtle() # Hide your turtle so you can see the pattern.

turtle.exitonclick()
