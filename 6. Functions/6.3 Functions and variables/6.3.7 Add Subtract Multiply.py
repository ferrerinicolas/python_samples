num1 = int (input("What is the first number: "))
num2 = int (input ("What is the second number: "))

x = num1
y = num2

def add(x,y):
    total = x +y
    print (str(x) + " + " + str(y) + " = " + str(total))
    
def substract(x,y):
    total = x - y
    print (str(x) + " - " + str(y) + " = " + str(total))

def multiply(x,y):
    total = x * y
    print (str(x) + " * " + str(y) + " = " + str(total))
    
operation = input ("Choose an operation (add, subtract, multiply): ")

if operation == "add":
    add(x,y)
    
elif operation == "subtract":
    substract(x,y)

elif operation == "multiply":
    multiply(x,y)