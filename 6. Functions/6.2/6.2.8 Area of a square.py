#Def function to print the calculated area of the square
def calculate_area(side_length=10):
    area = side_length * side_length
    
    print("The area of a square with sides of length " + str(side_length) + " is " + str(area))
    
#Input of user for the side length
user_length = int ( input ("Enter side length: "))

#if user length is less or equal than 0, use 10 as predeterminated
if user_length <= 0:
    calculate_area()

#Else use the value given by the user
else:
    calculate_area(user_length)