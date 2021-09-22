speed(5)

#Function to maque square
def make_square(square_length):
    for i in range(4):
        for i in range(4):    
            pendown()
            forward(square_length)
            left(90)
        forward(400)
        left(90)


        

        
        
penup()
setposition(-200,-200)
x = input("Type Square Length: ")
make_square(x)


"""
Write a program that has Tracy draw a square in each corner of the
canvas.
The user should give a one length dimension to be used for the sides
of all squares.

Hints:

Your sidewalk program may give you a bit of help with this program!
Save the user input in a variable named square_length.
"""