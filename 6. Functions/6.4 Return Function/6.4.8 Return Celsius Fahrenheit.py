# Write your function for converting Celsius to Fahrenheit here.
# Make sure to include a comment at the top that says what
# each function does!

def converting_c (f):
    c = (f-32) / 1.8
    return float(c)

# Now write your function for converting Fahrenheit to Celsius.

def converting_f (c):
    f = (1.8 * c) + 32
    return f


# Now change 0C to F:
print (converting_f(0))


# Change 100C to F:
print (converting_f(100))

# Change 40F to C:
print (converting_c (40))

# Change 80F to C:
print (converting_c (80))