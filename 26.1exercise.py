# Exercise -
# Q1. Write a code to sort the array in ascending order.
from array import *
vals = array('i', [5, 9, -8, 4, 2])
print(sorted(vals))

print('#>>>>>>>>>>>>>>>')
# Another way of sorting array -
arr = [5, 2, 9, 1, 7, 3]
arr.sort()
print('Sorted Array - ', arr)

print('# >>>>>>>>>>>>>>>>>>')
# Q2. Write a code to find a factorial of a given number.

# Finding factorial in a array
import array as arr
import math
numbers = arr.array('i', [3, 5, 7, 0, 1])

factorials = arr.array(numbers.typecode, (math.factorial(num) for num in numbers))

print('Original Array:', numbers)
print('Factorials Array:', factorials)

print('# >>>>>>>>>>>>>>>>')
# For Large factorials use list -
print('For Large factorials use list - ')
# Another way
import math

# list of numbers
numbers = [5, 10, 20, 50, 100]

# store factorials in a list
factorials = [math.factorial(num) for num in numbers]

print("Numbers:", numbers)
print("Factorials:")
for n, f in zip(numbers, factorials):
    print(f"{n}! = {f}")

print('# >>>>>>>>>>>>>>>')
# Finding Factorial from a user input
# Another way
print('Finding Factorial from a user input')
print('Factorial of a number')
from math import factorial
num = int(input('Enter a number: '))
print('Factorial of', num, 'is:', factorial(num))