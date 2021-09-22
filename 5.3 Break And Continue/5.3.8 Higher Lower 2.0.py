my_float = 3.3312
round(my_float,2)
# Your code here...

#Your code here...

while True:
    guess = float(input("Enter a guess: "))
    if round(guess,2) == round(my_float,2):
        print("Correct!")
        break
    elif guess > my_float:
        print("Too high!")
    else:
        print("Too low!")