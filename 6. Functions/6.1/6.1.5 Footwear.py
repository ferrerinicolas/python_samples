#Function will sandals boots for  sunny
def sunny():
    print ("On a sunny day, sandals are appropiate footwear.")

 #Function will print galoshes for the rainy   
def rainy():
    print ("On a rainy day, galoshes are appropiate footwear.")

#Function will print boots for the snowy
def snowy():
    print ("On a snowy day, boots are appropiate footwear.")


    

# Get input from the user and print matching greeting
# If other option, print that it is invalid    
weather = input ("What is the weather?: (sunny, rainy, snowy) ")
if weather == "sunny":
    sunny()
elif weather == "rainy":
    rainy()
elif weather == "snowy":
    snowy()
else:
    print("Invalid option.")