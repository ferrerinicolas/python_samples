# Amount of food and number of people
tons_of_food = 0.07
num_people = 25


print ("Number of people: " + str(num_people) + " Number of tons of food: " + str(tons_of_food))
# Determine how much food each person gets
tons_of_food_per_person = tons_of_food / num_people
print(tons_of_food_per_person)


# Ask the user how much food they took
tons_taken = float(input("How many tons of food did you take? "))

#Compare rounded information given.
if round(tons_taken,5) == round (tons_of_food_per_person,5):
    print("Good job, you took the right amount of food!")
else:
    print("You took the wrong amount of food!")