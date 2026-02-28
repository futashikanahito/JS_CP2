# JS, 1st, Fractal Pattern Generator

# ----- PSUEDOCODE -----
#set up all the turtle things
#define main function
#   define the actual creation triangle function
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# ----- PSUEDOCODE & CODE -----
from turtle import *

screen = Screen()
shape("turtle")
color("blue")
speed(0)
penup() 

def main():
    def create(length, i):
        if i == 0:
            for _ in range(3):
                forward(length)
                left(120)
            return
        half = length / 2
        create(half, i - 1)
        forward(half)
        create(half, i - 1)
        backward(half)
        left(60)
        forward(half)
        right(60)
        create(half, i - 1)
        left(60)
        backward(half)
        right(60)
        
    recursions = int(input("How many recursions do you want? "))
    length = 600

    teleport(-length / 2, -length / 2)
    pendown()
    create(length / 2, recursions)

main()
mainloop()