'''Exercise : Positive, Zero, or Negative?5 points
Write a program that asks the user for a number. Report whether that number is positive, zero, or negative.

An example interaction with your program might look like this:

Enter a number: -3
That number is negative!
… or this:

Enter a number: 5
That number is positive!
… or this:

Enter a number: 0
That number is zero!'''


user_number = int (input ("Please write a number: "))

if user_number >=1:
    print ("That number is positive!")

elif user_number < 0:
    print ("That number is negative!")
    
else:
    print ("That number is zero!")