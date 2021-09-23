#Def function to print the calculated area of the square
def calculate_area(side_length):
    print("The area of the square it is: " + str(side_length * side_length))

#Input of user for the side length
user_length = int ( input ("Enter side length: "))

#if user length is less or equal than 0, use 10 as predeterminated
if user_length <= 0:
    calculate_area(10)
    
#Else use the value given by the user
else:
    calculate_area(user_length)