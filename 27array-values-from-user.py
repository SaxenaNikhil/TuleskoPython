# Array -
# How do you create the array when you ask the user to enter the value and you don't know the size of the array

from array import *
arr = array('i', [])

n = int(input('Enter the length of the array - '))

for i in range(n):
    x = int(input('Enter the next value - '))
    arr.append(x)

print(arr)

# Find the index number of the value from the array
val = int(input('Enter the value for search - '))

# Finding the value through the manual method
k = 0
for e in arr:
    if e == val:
        print(k)
        break

    k+=1

print('# >>>>>>>>>>>>>>>')

# Finding the value through the in-built python function
print('Finding Index number of value from array:',arr.index(val))