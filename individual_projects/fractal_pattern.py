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


from turtle import *
import time

shape("turtle")
screen = Screen()
screen.tracer
color("blue")
speed(5)
penup()
teleport(500,-400)
setheading(180)
pendown()

def main():
    length = 1000
    positions = []
    recursions = input("how many recursions do you want? ")
    for i in range(int(recursions)):
        for _ in range(3):
            positions.append(tuple(position()))
            forward(length)
            right(120)
        length /= 2  
        penup()
        setheading(150)
        for x in range(len(positions)-1):
            p1 = positions[x-1]
            p2 = positions[x]
            teleport((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
        pendown()


main()

mainloop()