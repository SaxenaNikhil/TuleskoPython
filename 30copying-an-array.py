# Create another array from existing array using numpy
from numpy import *

arr = array([1, 2, 3, 4, 5])

# Now to add 5 to each element
# This is normal way.
for i in range(len(arr)):
    arr[i] += 5

print(arr)

print('# >>>>>>>>>>>>')

print('Using Numpy')

# Fast way to write the code using Numpy -
arr1 = array([1, 2, 3, 4, 5])
arr1 = arr1 + 5
print(arr1)

print('# >>>>>>>>>>>>')

# Adding two arrays
# This is also called as Vectorized Operation
print('Adding two arrays')

arr2 = array([1, 2, 3, 4, 5])
arr3 = array([6, 7, 8, 9, 10])

arr4 = arr2 + arr3

print(arr4)

print('# >>>>>>>>>>>>>>>')

#Find sum of an array
print('Find sum of an array')
arr11 = array([1, 2, 3, 4, 5])
total = sum(arr11)
print('Sum of array - ', total)

print('# >>>>>>>>>>>>>>>')

# Numpy num stands for numerical so we can perform mathematical operations such as trignometric operation which are - sin, cos, tan
# Find sin of an array
arr22 = array([1, 2, 3, 4, 5])
print('sin - ',sin(arr22))

# Find log of number in an array
print('log - ',log(arr22))

# Find sqrt of number in an array
print('sqrt - ',sqrt(arr22))

# Find sum of number in an array
print('sum - ',sum(arr22))

# Find min of number in an array
print('min - ',min(arr22))

# Find max of number in an array
print('max - ',max(arr22))

# Find unique number in an array
arr33 = array([11, 22, 33, 11, 44, 55, 33])
print('unique - ',unique(arr33))

# Find sort number in an array
arr44 = array([55, 33, 44, 22, 11])
print('sort - ',sort(arr44))

# Concatenate two arrays
arr55 = array([1, 2, 3, 4, 5])
arr66 = array([6, 7, 8, 9, 10])
print('Concatenate two arrays - ', concatenate([arr55, arr66]))

print('# >>>>>>>>>>>>>')
print('Concept of Copying an array - ')

# Concept of Copying an array -
arr66 = array([1, 2, 3, 4, 5])

# Wrong Method
# This looks like we have copied an array but in reality these two arrays have same address as both the array are pointing to the same address. This is also called as aliasing.
arr77 = arr66
print(arr66)
print(id(arr66))
print(arr77)
print(id(arr77))

print('# >>>>>>>>>>>>>')
print('Shallow Copy -')
# Now to create two different arrays
# view() is a function which will help you to create a new array at a different location. Here both the arrays have different address in ram
arr88 = arr66.view()
arr66[1] = 7

print(arr66)
print(id(arr66))
print(arr88)
print(id(arr88))

# Here we have two different types of copy - Shallow Copy and another is Deep Copy.
# Here in Shallow Copy it will copy the array but they are still dependent on each other. So if we change the value of at-least one element in the original array then the value in the other array will also change.
# view() uses shallow copy.
# Deep Copy - They are simply two different arrays after they are copied but they are not linked with each other in any way. In this case we use 'copy()' function.
print('# >>>>>>>>>>>>')
print('Deep Copy - ')
arr222 = array([2, 6, 8, 1, 3])
arr333 = arr222.copy()

arr222[1] = 7

print(arr222)
print(id(arr222))
print(arr333)
print(id(arr333))
# Deep copy gives different addresses and also the arrays are not dependent on each other.
