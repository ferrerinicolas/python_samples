ingredient_1 = input("Enter ingredient 1: ")
ounces_1 = float(input("Ounces of " + ingredient_1 +":"))

ingredient_2 = input("Enter ingredient 2: ")
ounces_2 = float(input("Ounces of " + ingredient_2 +":"))

ingredient_3 = input("Enter ingredient 3: ")
ounces_3 = float(input("Ounces of " + ingredient_3 +":"))

number_servings = int (input("Number of servings: "))

total_ounces_1 = number_servings * ounces_1
total_ounces_2 = number_servings * ounces_2
total_ounces_3 = number_servings * ounces_3

print ("Total ounces of " + ingredient_1 +": " + str(total_ounces_1))
print ("Total ounces of " + ingredient_2 +": " + str(total_ounces_2))
print ("Total ounces of " + ingredient_3 +": " + str(total_ounces_3))