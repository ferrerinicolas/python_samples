
# Add your own tests here
def replace_at_index(string, index, letter):
    
    return string[:index] + str(letter) + string [index+1:]
    
print (replace_at_index("house", 0, "m"))
# => "mouse"
print (replace_at_index("door", 3, "t"))
# => "doot"

