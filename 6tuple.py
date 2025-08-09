# Tuple is immutable, as we cannot change the value of it
# For tuple we use round bracket ()
print('Tuples in Python ')
tup = (21, 36, 14, 25) # Now since we have specified it so we cannot change the value of it.
print(tup)

# Now to access the value from the tuple
print('Value of tuple at index 1 - ', tup[1])

# Now we will try to change the value of the tuple at index 1
# Since it's immutable so it won't change and will give the error.
# tup[1] = 33
# Error - 'tuple' object does not support item assignment.

# Note - So basically, tuple is like a list but you cannot change the value of it.
# When to use tuple? - You have the list and you don't want to change the values of it.
# Now since we don't change the values in tuple so iteration in tuples is faster than in list.

# SET in Python

print('-----------------------')
print('Set in Python ')
print('Now we will look at Set in Python ')

# It is simply a collection of unique elements
# For Set we use curly bracket {}
s = {22, 25, 14, 21, 5}
print('Value of set s - ', s)
# so printing the value of set prints the random values and there is no sequence of the values in a set

s1 = {25, 14, 98, 63, 75, 98}
print('Value of set s1 - ', s1)
# Here the set s1 removed the duplicate values in the set
# Set uses the concept of 'hash' which helps in improving the performance as we want to fetch the element as fast as possible, so it does not follow the sequencing when we print the set values.

# Using the index number to access the set value is not possible as the sequencing is not followed in set, so even if you try to print the value then it will give the error.
# print(s[2])

# functions in set
# add, remove, pop etc..
# you can play around with these function to test these out.
