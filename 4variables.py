name = 'youtube'
print(name)

print(name[0])
print(name[1])
print(name[2])
print(name[6])
print('-----------------')
print(name[-1])
print(name[-7])
print('-----------------')
print('The first two characters - ' + name[0:2]) # this starts at 0 and ends at 1
print('Printing some characters - ' + name[1:4]) # this starts at 1 and ends at 3
print('Printing some characters - ' + name[1:]) # this starts at 1 and continues till the end
print('Printing some characters - ' + name[:4]) # this ends at 3
print('Printing some characters - ' + name[3:10]) # this will start at 3 but since it does not have the 10 characters so it will end at the last character of the word.

# String in Python is immutable as once you have assigned the value of the variable as string you cannot change even a character in the variable.
# So this below will give error -
# name[0:3] = 'my'
# name[0] = 'R'

# This says 'str' object does not support item assignment

# Adding word to the custom name variable
print('my ' + name[3:])

# check the length of the string
print('length of name variable : ' + name + ' is - ', len(name))


