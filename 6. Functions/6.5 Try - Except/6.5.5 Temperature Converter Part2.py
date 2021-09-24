# Write your function for converting Celsius to Fahrenheit here.
# Make sure to include a comment at the top that says what
# each function does!

def converting_c (c):
    f = (1.8 * c) + 32
    return float(f)

# Now write your function for converting Fahrenheit to Celsius.

def converting_f (f):
    c = (f-32) / 1.8
    return c

try:
    userC = float (input("Write Celsius to be converted on F: "))
    userF = float (input("Write Fahrenheit to be converted on C: "))
    print (str(userC) + "C* Converted to Fahrenheit it is: " + str(converting_c(userC)))
    print (str(userF) + "F* Converted to Celsius it is: " + str(converting_f(userF)))

except ValueError:
    print("That't not a float to be converted")