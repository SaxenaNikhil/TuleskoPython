# Exercise - Write a code to find the cube of the number. Take the input from the user using input().
from math import pow

userInput = int(input('Enter a number to find the cube of the number - '))

#Using pow function from math to find the cube of the number.
cube = pow(userInput, 3)
print('Cube of the number is - ', cube)