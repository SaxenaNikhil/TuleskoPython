# For loop for array
x = ['navin', 65, 2.5]

for i in x:
    print(i)

# Here we don't initialise the variable, neither we take the condition and also we don't increment or decrement it. As it will be dont by for loop itself here.

# Note - If you want to print all the values from the list then use the for loop.

# >>>>>>>>>>>>>>>>

print('# >>>>>>>>>>>>>>>>')

# For loop for word
y = 'NAVIN'
for i in y:
    print(i)

# Note we can use for loop for 'tuple' and for 'set' as well.

# >>>>>>>>>>>>>>>>
print('#>>>>>>>>>>>>')

# Now we want to print the values from 1 to 10. So for that we have to use range here.

for i in range(10):
    print(i)

# Here range(10) means start at 0 and end at 9

print('#>>>>>>>>>>>')

# Note - In range we can start from different values as well. let's say we want to print from 11 to 20 in that case we will start from 11 and end at 21 because we want to include 20 as well and we will also have 1 so that we know the difference in the iteration for this it will be 1 as we want to print all the values from 11 to 20.

# Now if the 1 is 2 here in the end in range then the difference in the iteration will be 2 which means gap of 2.

for i in range(11,21,1):
    print(i)

print('# >>>>>>>>>>>>>>>>')

for i in range(1, 11, 2):
    print(i) # Here the gap will be of 2

# Now to print the number in reverse the order in the range will be reverse and the difference will be -1 as its in reverse. So we want to print from 20 down to 11 so the range will be 20 to 10 as we want to include the number 11 as well. So it will be like -
print('# >>>>>>>>>>>>>')
for i in range(20,10,-1):
    print(i)

# >>>>>>>>>>>>>>>>>>>>

print('# >>>>>>>>>>>>>')
# Print the values from 1 to 20 and skip those which are divisible by 5
for i in range(1, 21):
    if i%5!=0:
        print(i)