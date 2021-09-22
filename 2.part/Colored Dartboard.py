print("this is my third commit")
speed(5)
radius = 100
circle_quantity = 4

#this function make circles
def make_circle():
    pendown()
    color(color_choice)
    begin_fill()
    circle (radius)
    end_fill()
    penup()
    
#This function will move tracy to next circle
def move_down():
    penup()
    left(90)
    forward(25)
    right(90)
    pendown()
        
penup()
setposition(0,-100)
#Here we take the colors from input
for i in range(4):
    color_choice = input("Which color for the circle?: ")
    make_circle()
    radius = radius - 25
    move_down()
    