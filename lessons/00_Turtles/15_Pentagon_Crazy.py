import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

tina = turtle.Turtle() 
tina.color("blue") 
                # Create a turtle named tinatina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)
tina.goto(-150,0)
tina.color("blue")
tina.begin_fill()
tina.forward(300)
tina.left(160)
tina.forward(300)
tina.left(160)
tina.forward(300)
tina.left(160)
tina.forward(300)
tina.end_fill ()
tina.goto(-90,225)
tina.write("Mr.Blake & Evan Sheinberg")
turtle.pensize(-70)
turtle.exitonclick()