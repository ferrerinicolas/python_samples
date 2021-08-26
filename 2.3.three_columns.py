"""
Use for loops to enhance the ‘4 Columns’ program you wrote in our last lesson.
Remember:

Your entire code does not have to be a part of your loop
Pay careful attention to your indentation!
Hint: Send Tracy from her home in the center to her starting position to draw your lines and then write your loop to draw all three!
"""
import turtle
import turtledemo
from turtle import forward, left, penup, pendown, backward

penup()
backward(200)

for i in range (3):
    forward(100)
    left(90)
    penup()
    forward(200)
    left(180)
    pendown()
    forward(400)
    penup()
    backward(200)
    left(90)