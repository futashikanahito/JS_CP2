# JS, 1st, Fractal Pattern Generator

# ----- PSUEDOCODE -----
# Create turtle setup function
    # set turtle to turtle shape
    # ask user what color for the turtle
    # ask user the recursion depth
    # ask user what color for the background
    # ask user which fractal to do
# Create Sierpinski gasket function
    # 
# Create Sierpinski carpet function
    # 


import turtle
import time

turtle.shape("turtle")
screen = turtle.Screen()
screen.tracer
turtle.color("blue")
turtle.penup()
turtle.forward(500)
turtle.left(90)
turtle.backward(450)
turtle.left(90)
turtle.pendown()

def build_tri():
    for _ in range(3):
        turtle.forward(1000)
        turtle.right(120)

    
build_tri()

time.sleep(5)