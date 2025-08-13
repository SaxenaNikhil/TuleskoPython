# Exercise -
# Q1. Print first 50 fibonacci numbers.
a, b = 0, 1
count = 0
while count<50:
    print(a)
    a, b = b, a+b
    count += 1

print('# >>>>>>>>>>>>>>>>')

# Now using the concept of break, continue or pass
x, y = 0, 1
i = 0

while True:
    if i >= 50:
        break

    if i<0:
        continue

    print(x)
    x, y = y, x+y
    i += 1

# Q2. Check a given number is prime or not.
from math import sqrt

num = int(input('Enter a number - '))
c = int(sqrt(num))

# 1 is neither prime nor composite
if num <= 1:
    print('Not a prime number')
else:
    for i in range(2, c+1):
        if num%i == 0:
            print('Not a prime number')
            break
    else:
        print('Prime Number')