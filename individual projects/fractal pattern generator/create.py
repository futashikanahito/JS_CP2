# import all needed libraries
from turtle import *

# ---

# define create function
#   create base case
#   go to the right position
#   print the bottom left triangle
#   go to the right position
#   print the bottom right triangle
#   go to the right position
#   print the top triangle
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