# Exercise -
# Q1. Create an array with 5 values and delete the value at index number 2 without using the in-built function.

from array import *
arr = array('i', [12, 13, 14, 15, 16])

# Get the index at which you want to delete the video
delete_index = 2

# shift elements to left starting from delete_index until the length of array -1 because we want to remove one element.
for i in range(delete_index, len(arr)-1):
    arr[i] = arr[i+1]

# remove the last element (since it's now duplicate)
arr = array('i', arr[:-1])

print('Array after deletion', arr)

# I have used this code - array('i', a[:-1]) so that i can slice the last element from the array.

# Q2. Write a code to reverse an array without using in-built function.

arr1 = array('i', [10,20,30,40,50])

n = len(arr1)

# Here in n // 2 loop runs till half the array
for i in range(n // 2):
    # swap a[i] with a[n-1-i]
    # Swap the first and last, then second and second-last, and so on.
    arr1[i], arr1[n-1-i] = arr1[n-1-i], arr1[i]

print('Reversed Array - ', arr1)