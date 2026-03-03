# JS, 1st, Fractal Pattern Generator

# ----- PSUEDOCODE -----

# --- main.py ---
# import all needed libraries & files
# set up all turtle variables for printing
# ask user for background color and # of recursions
#--
# define main function
#   print generating triangle
#   teleport to bottom left of triangle 
#   call create.py's create function
#   print finished triangle
#   ask if user would like to save as an image
#   if they do:
#       call save_image.py's save function
#   exit the program

# --- create.py ---
# import all needed libraries
#--
# define create function
#   create base case
#   go to the right position
#   print the bottom left triangle
#   go to the right position
#   print the bottom right triangle
#   go to the right position
#   print the top triangle

# --- save.py ---
# import all needed libraries
# define save function
#   take a screenshot through python ¯\_(ツ)_/¯

# ----- PSUEDOCODE & CODE -----

# import all needed libraries & files
# set up all turtle variables for printing
# ask user for background color and # of recursions
from turtle import *
import save_image
import create

screen = Screen()
shape("turtle")
speed(0)
penup()

print_color = input("What color do you want the fractal to be? ")
while True:
    try:
        color(print_color)
        break
    except:
        print_color = input("What color do you want the fractal to be? ")

bg_color = input("What color do you want the background to be? ")
while True:
    try:
        bgcolor(bg_color)
        break
    except:
        bg_color = input("What color do you want the background to be? ")

recursions = int(input("How many recursions do you want? "))
length = 600

# ---

# define main function
#   print generating triangle
#   teleport to bottom left of triangle 
#   call create.py's create function
#   print finished triangle
#   ask if user would like to save as an image
#   if they do:
#       call save_image.py's save function
#   exit the program
def main():
    print("Generating Sierpinski Triangle...")

    teleport(-length / 2, -length / 2)
    pendown()
    create.create(length / 2, recursions)
    hideturtle()

    print("Fractal generated successfully!")

    save = input("Would you like to save your image as a png (y/n)? ")
    if save == "y":
        save_image.save()
    
    input("Press Enter to exit the program...")
    exit()

main()
mainloop()