"""
Use for loops to enhance the ‘4 Columns’ program you wrote in our last lesson.
Remember:

Your entire code does not have to be a part of your loop
Pay careful attention to your indentation!
Hint: Send Tracy from her home in the center to her starting position to draw your lines and then write your loop to draw all three!
"""

from turtle import *

def set_position():
    penup()
    setposition(0,-100)

set_position()

speed(10)

def make_circle(x=3):
    
    for i in range(x):
        pendown()
        circle(10)
        penup()
        forward(20)
        left(10)

make_circle(36)

setposition(0,0)



