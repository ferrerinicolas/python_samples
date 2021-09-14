"""
Use for loops to enhance the ‘4 Columns’ program you wrote in our last lesson.
Remember:

Your entire code does not have to be a part of your loop
Pay careful attention to your indentation!
Hint: Send Tracy from her home in the center to her starting position to draw your lines and then write your loop to draw all three!
"""
#import turtle
from turtle import *

speed(5) 
penup()


def make_figure(radius):
    pendown()
    begin_fill()
    color("red")
    for i in range(4):
        forward(radius)
        left(90)
    color("blue")
    circle(radius)
    end_fill()
        
setposition (0,-100)
radius = input ("Inserte el radio de las figuras: ")
make_figure(radius)

