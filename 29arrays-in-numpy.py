# Different ways of creating an array in numpy
# There are six ways - 1. array(), 2. linspace(), 3. logspace(), 4. arange(), 5. eros(), 6. ones()

#Method 1 Arrays
from numpy import *

arr = array([1, 2, 3, 4, 5])
# The type of this array is int64

arr1 = array([10, 20, 30, 40, 50.0])
# for array([10, 20, 30, 40, 50.0]) - the type of this array is float64

# To check the type of the array -
print(arr.dtype)
print(arr)

print(arr1.dtype)
print(arr1) # Here in the output you will see that every value here will be converted into float which is an implicit conversion as it sees the float value in the array so it converted the other values to float as well. [10., 20., 30., 40., 50.]

# Having int values in the array but mentioning that we need float values in the array then we see the output as -
arr2 = array([23, 32, 45, 54, 60], float)
print(arr2.dtype)
print(arr2) # [23. 32. 45. 54. 60.]
# Here we get the float values instead of int as it will convert into float

print('# >>>>>>>>>>>')

# Method 2
print('Array using linspace() - ')
# linspace() takes 3 parameters which are : Start, Stop, Step
arrlin = linspace(0, 15, 16)
# Here the stop value 15 is also included in this.
# Here the value 16 is not step value but basically it's the number of parts you want to go for. Here 16 will break the range into 16 different parts. Here 16 will break all the range into 16 different parts so it will run from 0 to 15 and all the values here are float. They are float values because we are breaking the parts into float values.
# Here the output is - [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15.] because all the values here

print(arrlin)

print('# >>>>>>>>>>>>>')

# Check for more parts values -
# This will give float values in the array.
arrlin1 = linspace(0, 15, 20)
print(arrlin1)

print('# >>>>>>>>>>>>>')

#Note - If we don't specify the parts then it will give us 50 parts
arrlin2 = linspace(0, 15)
print(arrlin2)

print('# >>>>>>>>>>>>>')

# Method 3
print('Array using arange() - ')
# Arguments - (first element, second element, step)
# So here the step will work like - print first number, step will skip the number by the number of times which is mentioned in step.
# So here below it has skipped the value by 2 after printing the first value.
arrstep = arange(1, 15, 2)
print(arrstep)

print('# >>>>>>>>>>>>>')

# Method 3
print('Array using logspace() - ')

# They are different from linspace(), but unlike the linspace logspace. Just like linspace() logspace() also creates parts, where we breakdown the range into number of parts.
# They are different from linspace(), but unlike the linspace logspace. Just like linspace() logspace() also creates parts, where we breakdown the range into number of parts. But in linspace() the gap between two elements is fixed.
# But in logspace() the space between two numbers will be log of it. So it will start from 10 raised to 1; to 10 raised to 40 and it be divided into 5 parts

arrlog = logspace(1, 40, 5)
print(arrlog)
# So here it started from 10 raised to 1 and ended at 10 raised to 40 and rest all numbers are in between.
# lets print the first element here in normal format where after decimal point we have two digits.
print('%.2f' %arrlog[0])
print('%.2f' %arrlog[4]) # The number printed will be somewhere around 40 digits after 10

print('# >>>>>>>')

# Method 4
print('Array using zeros() - ')
# To create the array of size 10 and all the values by default should be zero then in that case you should be using zeros as a function. So i'll be using zeros we have to specify the size of it.
# It will create an array of 5 will all the number as zeros
# By default it gives float values for int you have to mention like - (5, int)
arrzeros = zeros(5)
print(arrzeros)

arrzeros0 = zeros(3, int)
print(arrzeros0)

print('# >>>>>>>>>>>')

#Method 5
print('Array using ones() - ')
# Same as zeros it will give all the values as ones
# By default it gives float values for int you have to mention like - (5, int)
arrones = ones(5)
print(arrones)

arrones1 = ones(3, int)
print(arrones1)