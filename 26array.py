# Array

# This is one way of importing array using arr as alias
#import array as arr
#arr.array()

# This means you want to import all the properties from array
from array import *
# hare we have taken variable vals which is basically values. so vals is an array. In this array you have to specify two things - one is the 'type' and second is the 'values'.
# Moreover all the values should be of same type if we have int array then all the values should be int. So to mention that in an array you have to use typecode. So typecode means every type will have a unique code. Such as integer has types where we have byte, long and int.

# So the range of integer is from negative to positive. Now if you have to only store a positive value only then you will go for 'unsigned' integer because it starts with 0 and ends at a particular value. So for unsigned we have to use 'I'

# Table for TypeCode

# Typecode - C Type - Python Type - Min. Size in bytes
# 'b' - signed char - int - 1
# 'B' - unsigned char - int - 1
# 'u' - Py_UNICODE - Unicode character - 2
# 'h' - signed short - int - 2
# 'H' - unsigned short - int - 2
# 'i' - signed int - int - 2
# 'I' - unsigned int - int - 2
# 'l' - signed long - int - 4
# 'L' - unsigned long - int - 4
# 'f' - float - float - 4
# 'd' - double - float - 8

# I want to create an array of integers - so i will use 'i'. And as this is a signed integer so we can also have negative values as well in the array.
vals = array('i', [5, 9, -8, 4, 2])

print(vals)

# Error due to float value
# Now in the above array we make the number in array as float such as 8.5 instead of 8 then this will throw an error.
#vals1 = array('i', [5, 9, 8.5, 4, 2])
#print(vals1)

# Error due to negative value
# Using Unsigned int and putting negative value in this then it will give an error
#vals2 = array('I', [5, 9, -8, 4, 2])
#print(vals2)

# Note - Whenever you create an array mention a proper typecode.

# To Get the size of an array use 'buffer_info()' method and this returns a tuple which has a address of the array and second parameter is the size of an array.
print(vals.buffer_info())

# To get the type of the array use 'typecode'
print(vals.typecode)

print('# >>>>>>>>>>>>')
# To get the length of the array use 'len()'
print(len(vals))

# To add a value use - append()
# To remove a value use - remove()

print('# >>>>>>>>>>>>')
# To reverse an entire array use - reverse()
vals.reverse()
print(vals)

print('# >>>>>>>>>>>>')
# Now to print the value one by one and not al-together
print(vals[0])

print('# >>>>>>>>>>>')
print('Print the value of array one by one using for loop in range in length of array i.e. len(vals)')
# Using the loop to print the value one by one. Also len(vals) get the length of the vals array
for i in range(len(vals)):
    print(vals[i])

print('# >>>>>>>>')
print('Another way to print the values from an array - ')
# Another way to print the values from an array
for e in vals:
    print(e)

print('# >>>>>>>>>>>')

# Working with Characters in an array
print('Working with Characters in an array - ')
charvals = array('u', ['a', 'e', 'i'])
print(charvals)
print(charvals.buffer_info())

print('# >>>>>>>>>>>')

# Create a new array with the same values
print('Create a new array with same value from another array')
# This takes the typecode and from 'a for a in vals' this loop takes one value at a time from vals and assign it to the array.
newArr = array(vals.typecode, (a for a in vals))

for e in newArr:
    print(e)

print('# >>>>>>>>>>')
# To assign a square of a number to a new array from an existing array.
sqrArr = array(vals.typecode, (a*a for a in vals))

for e in sqrArr:
    print(e)