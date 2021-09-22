#Ask the user for quantity of name he has and save it in a variable
number_of_names = int (input ("How many names do you have?: "))
full_name = ""

#Print many times as the name of the user
for i in range (number_of_names):
    f_name = str(input("Write your names: "))
    #Save each name and write a space between them
    full_name = full_name + f_name + " "

#Print out all the names saved 
print (full_name)
    
