average = 0
new_score = 0

for i in range(3):
    test_score = int (input ("Write the score:"))
    new_score = new_score + test_score

average = new_score / 3
print("The average it is: " + str(average))