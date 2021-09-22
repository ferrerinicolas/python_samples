
# Try changing these, and see what happens!
category = 3
tests_per_person = 3
name= ""
# For each person, get name and test scores
for i in range(category):
    name = input("Enter a category: ")
    my_string = ""
    
    # Add up the test scores
    for j in range(tests_per_person):
        something = input("Enter something in that category: ")
        my_string = my_string + something
        
    # Calculate and print average score
    average = my_string
    
    print( name + ": " + my_string)