# Prime numbers - These are the concepts which are divisible by 1 or itself. Such as 2, 5, 7, 13, 17

# The concept is that it should not be divisible starting from 2 upto the num then its a prime number. So here range is from 2 to num where num is not included.

num = 5
for i in range(2, num): # this goes from 2 to 6
    if num % i == 0:
        print('Not a prime number')
        break
else:
    print('Its a prime number')

print('# >>>>>>>>>>')

# finding the prime number using the sqrt

from math import sqrt
num1 = 991
limit = int(sqrt(num1)) + 1
for i in range(2, limit):
    if num1 % i == 0:
        print('Not a prime number')
        break
else:
    print('Its a prime number')