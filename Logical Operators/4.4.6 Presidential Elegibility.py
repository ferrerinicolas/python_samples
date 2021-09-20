
user_age = int ( input ("Tell us your age: "))
born_usa = input ( "Born in the U.S? (Yes / No): ")
years_residency = int (input ("Years of Residency: "))

if user_age >= 35 and years_residency >=14 and born_usa == "Yes":
    print ("You are eligible to run for president!")

else:
    print ("You are not eligible to run for president")
if user_age < 35:
    print ("You are too young. You must be at least 35 years old.")
if born_usa == "No":
    print ("You must be born in the U.S. to run for president.")
if years_residency <14:
    print ("You have not been a resident for long enough.")