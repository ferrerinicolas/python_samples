magic_number = 3
#Your code here...

while True:
    guess = int(input("Enter a guess: "))
    if guess == magic_number:
        print("You got it!")
        break
    elif guess > magic_number:
        print("Too high!")
    else:
        print("Too low!")

