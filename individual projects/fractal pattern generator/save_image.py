# import all needed libraries
from PIL import ImageGrab
from turtle import *

# ---

# define save function
#   take a screenshot through python ¯\_(ツ)_/¯
def save():
    canvas = getscreen().getcanvas()
    x = canvas.winfo_rootx()
    y = canvas.winfo_rooty()
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    ImageGrab.grab(bbox=(x, y, x + width, y + height)).save("fractal.png")