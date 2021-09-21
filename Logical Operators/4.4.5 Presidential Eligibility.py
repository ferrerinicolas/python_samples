#Ask User for his age, if born in USA and years of residence and save it in variables
user_age = int ( input ("Tell us your age: "))
born_usa = input ( "Born in the U.S? (Yes / No): ")
years_residency = int (input ("Years of Residency: "))

#If all the conditions are correct, print out 
if user_age >= 35 and years_residency >=14 and born_usa == "Yes":
    print ("You are eligible to run for president!")

#if any of the conditions doesnt work, say he cant.
else:
    print ("You are not eligible to run for president")