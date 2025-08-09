a = 5
b = 6

# Using 3rd variable to swap the values
#temp  = a
#a = b
#b = temp

#print(a)
#print(b)

# >>>>>>>>>>>>>>>>>>>>>
# Swaping values without using third variables.

#a = a + b # a=11
#b = a - b # b=5, a=11
#a = a - b # a=6

#print(a)
#print(b)

# Here the issue with this one is that a = 5 is 3 bits which is '101' and b = 6 is also 3 bits which is '110' but at a = a + b this is 4 bits which is '1011' so we are wasting 1 extra bit to swap the value.

# So to optimise this solution we have one more way which is XOR so we won't be wasting extra memory in this one.
# XOR to swap the values

#a = a ^ b
#b = a ^ b
#a = a ^ b

#print(a)
#print(b)

# >>>>>>>>>>>>>>>>>>>>

# There is another way to swap the numbers in python which is basically called 'ROT TWO'
# ROT TWO to swap the variables so basically it will swap the two top most stack items.

a,b = b,a

print(a)
print(b)