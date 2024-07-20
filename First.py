#This is how you write a comment
"""
This is a comment
Written in
more than just one line
"""
import sys

print("Hello, World!")

#This displays the python version
print(sys.version)

"""
Indentation In python is 
important as it is viewed as 
a block of code as opposed to 
just readablitity reasons
"""
x = 25
y = 45
z = "This is the value of a variable"
if x < y:
    print("X is not greater than Y!")
#else:
#    print("Y is greater than X!")

print(z)

ab = 5
ac = "John"
print(ab, ac)

#If data type is not specified a variable's data type can be changed
ba = 86
ba = "Josh"
print (ba)

# Use casting to specify a variable's data type
ca = str(3) # This will be '3'
cb = int(3) # This will be 3
cc = float(3) # This will be 3.0

# to get a viables type use the type() function
da = 5
db = "Tom"
dc = 6.0
print(type(dc))
print(type(da))
print(type(db))

# A string variable can be declared with either single or double quotation marks
ea = "Slim Jim"
eb = "lil John"
print(ea, "and", eb, "are the same lizard")

# Variable names are case sensitive 
a = 2
A = "Bob"
print ("a is equal to", a, "whereas A is equal to", A)