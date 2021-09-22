
penup()
setposition(0,-100)
pendown()
radius = int (input("Wright 20 for radius: "))
line = 0


#HOW TO START LOOP 0 FINISH 6

#Function to make figures increasing value of i in 1 until it reach 7 of range
for i in range(0,7):
    circle (radius ,360, line)
    radius = radius + 20
    line = line + 1



"""Write a program that will draw 7 shapes.
Your shapes should:

Start with 0 points
Each increase the number of points by 1 (ie: line- 2 points, triangle-
3 points, square- 4 points, etc.)
Start with a radius of 20 and increase in radius by 20 pixels each time
All be drawn from the same starting position
Hint: It is difficult to use the value of i to control both the radius of
the shape and the number of points so you may use a variable
called radius to control this.
"""