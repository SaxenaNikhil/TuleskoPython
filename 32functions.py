# Functions in Python
# Why we need functions - ? To make certain code re-usable so we create custom functions. Defining and calling the functions. Syntax for function is 'def'. So we write it as - def greet():

# Function definition
def greet():
    print('Hello')
    print('Good Morning')

# Function calling
greet()

# We can allocate some repititive task to function to help achieve a bigger task

print('# >>>>>>>>>>>>>>>')

print('Execute task from the function')
# Execute task from the function
# Add two numbers -
def add(x, y):
    c = x + y
    print(c)

add(2, 3)

print('# >>>>>>>>>>>>>>>>>>>')

print('Expecting return from the function')
# Expecting return from the function
# Now to return the value from the function so that we print value out of the function
def add1(x, y):
    return x + y

result = add1(5, 4)
print(result)

print('# >>>>>>>>>>>>>>>>>>')
print('Returning two values from the function')
# Returning two values from the function
def add_sub(x, y):
    a = x + y
    b = x - y
    return a, b

output1, output2 = add_sub(8, 7)
print(output1, output2)

# Note -  Always create function for the small tasks