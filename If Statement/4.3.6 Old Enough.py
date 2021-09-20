'''Exercise : Old Enough to Vote?5 points

Write a program that reports whether or not someone is old enough to vote 
in the U.S. You should do the following in your program:

Ask the user for their age, and store it in a variable
Use an if/else statement with the proper comparison operator to print 
You are old enough to vote! if the person’s age is at least 18, and 
You are not old enough to vote. otherwise
An example run of your program might look like this:

Age: 19
You are old enough to vote!
… or like this:

Age: 16
You are not old enough to vote.'''


user_age = int (input ("Please Write your age: "))

if user_age >= 18:
    print ("You are old enough to vote!")

else:
    print ("Your are not old enough to vote.")