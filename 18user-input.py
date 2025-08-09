# Getting user input in python
# Note here the input will always give you the value in string type after taking input from user. But here we are expecting the integer value as we want to do the arithmetic operation.

#x = input(" Enter 1st number: ")
# type conversion from string to integer
#a = int(x)

#y = input("Enter 2nd number: ")
# type conversion from string to integer
#b = int(y)

#z = a + b
#print(z)

# >>>>>>>>>>>>>>>>>>>>>>>>

# Best way to optimise this above solution is -
# Here we are doing the type conversion directly in the input and without using any other variable.
#x = int(input(" Enter 1st number: "))
#y = int(input("Enter 2nd number: "))
#z = x + y
#print(z)

# Lets take the input from the user in CHAR format.
# We need only a character and not a string from the user input so we want to control this scenario. So we take the zero index from the input using this - '[0]'
#ch = input('Enter a char - ')[0]
#print(ch)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Using EVAL function for evaluating an expression.

# Note - We can also use the function called 'eval' which will evaluate the function you are passing.
result = eval(input('Enter an expression - '))
print(result)
# For example try - 2 + 6 - 1, eval will evaluate this and will give the output as 7.

# >>>>>>>>>>>>>>>>>>>>>

# Exercise - in the 18.1 file check