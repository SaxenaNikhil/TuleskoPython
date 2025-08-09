# i want to find the square root of a number.

# x = sqrt(25)
# print(x)
# Here we got an error because of sqrt not defined. Here we need to ask for the import and export and in this we need access to modules here which is basically 'math'
import math
x = math.sqrt(25)
print(x)

# Floor function - Here what happens is, this function the value of the number is rounded of to to the lowes numeric value. So If the number is >=2.5 then it will not be rounded of to the next integer which here is 3 but if its less than 2.5 then it will be 2
print(math.floor(2.6)) # Answer is 2
print(math.floor(3.4)) # Answer is 3

# Ceil Function - Here what happens it in the ceil function the value of the number is rounded of to the higher numeric value.
print(math.ceil(2.2)) # Answer is 3
print(math.ceil(3.7)) # Answer is 4

# Power function -
print(math.pow(3, 2)) # 9

# Note its better to use the function instead of anything else.

# Also we have some constants in this math function as well and it's not just about functions. Such as we need to know the exact value of pi.
#Constant Values -
print(math.pi) # This prints the constant value of pi.
print(math.e) # This prints the value of epsilon

# >>>>>>>>>>>>>>>>>>>>>>>>>>

# Concept of Alias -
# If we are looking to use the short form of 'math' as 'm' then we need to use the concept of alias.
import math as m
print(math.sqrt(25))
print(m.sqrt(25))

# Now instead of importing a big 'math' library we only want to access only the specific functions such as we need to import only 'sqrt' and 'power'. So in this case you don't need to use the math function as well to access the function. Because you can use it directly.
from math import sqrt, pow
print(pow(4,5))

# Now to read documentation of math function on this -
help(math)
# This gives all the functions that you can use for the math function.

