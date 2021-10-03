""" This is the Scratchpad!
This file is not graded, but you can use it to test your code.

You can write and test your function in the Scratchpad, but make
sure to copy and paste it into the Unit Test file before checking
your answer. Remember to only copy and paste the function you want
to submit, not all of your tests.
"""

# Add your own tests here
# with the character at `index` replaced with a dash (-)
def replace_at_index(string, index):
   return string[0:index]+"-"+string[index+1:]

print(replace_at_index("eggplant", 3))
print(replace_at_index("strange", 0))
