# Write a code to check a given number is positive or negative

num = -2
if num > 0:
    print('Number is positive')
else:
    print('Number is negative')

# Take Three values from user and find the greatest number from them
v1 = int(input('Input 1st number - '))
v2 = int(input('Input 2nd number - '))
v3 = int(input('Input 3rd number - '))

if v1 > v2 and v1 > v3:
    print('v1 is greater')
elif v2 > v1 and v2 > v3:
    print('v2 is greater')
else:
    print('v3 is greater')