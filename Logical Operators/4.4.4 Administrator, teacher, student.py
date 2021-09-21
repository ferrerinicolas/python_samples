#Ask User for his role and save it in a variable
role = input ("Are you an administrator, teacher, or student?: ")

#If role "administrator or teacher" print they have keys
if role == "administrator" or role == "teacher":
    print ("Administrators and teachers get keys!")
    
#If role "Student" print they dont get keys
elif role == "student":
    print ("Students do not get keys")

#Else of the options, say the roles that can be used
else:
    print("You can only be an administrator, teacher, or student!")