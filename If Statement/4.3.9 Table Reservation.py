'''Write a program that asks the user for their name using input.
It should have another string variable that represents the name
on a particular table reservation in a restaurant, stored in a variable 
called reservation_name. The program should print Right this way! 
if the user’s name matches the name on the reservation, 
and Sorry, we don't have a reservation under that name. otherwise.

An example run of your program might look like this:

Name: Shonda
Right this way!
… or like this:

Name: Mel
Sorry, we don't have a reservation under that name.'''

#Ask user for his name to check on reservation
user_name = str(input ("Name: "))
reservation_name = "Nico"

#If its the name on reservation , print out
if user_name == reservation_name:
    print ("Right this way!")
    print (type (reservation_name))
    
#If not the name on reservation
else:
    print("Sorry we don't have a reservation under that name.")