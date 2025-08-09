# List is a collection of elements which means it is basically an ordered list where all the elements are in sequence
# Set is basically list which doesn't maintain the sequence

# So it depends if you want to go for all the values so you go for List and if you want the unique elements then you will go for Set.
# You can fetch the values in the list with the help of index numbers.


# Dictionary in Python
# Now to use the concept of key and value where you have the key and a value so every value will have a special key given by you. So to achieve you need to use the concept of dictionary.
# We will use curly brackets {}, in this we will specify both key and value
# We can use any key here, its just that the key should be immutable type and unique. You can use string, or numbers.

# Let see the example of dictionary -
data = {1:'Navin', 2:'Kiran', 4:'Harsh'}
print(data)

# How to fetch a particular value.
# If you want to fetch a particular value such as Harsh
print('Fetching a particular value such as Harsh:', data[4])

# Now if you try to print for the key which is not available in dictionary then it will throw an error such as lets try for the key 3
# print('This will throw an error - ', data[3])

# Another way of fetching these values are -
print('Another way for fetching values - ', data.get(1))

# Since the value for the key at 3 is missing so it prints None.
print('Printing the value of the missing index from dictionary -', data.get(3))

# Now what if we want to print the value of the key which is missing.
print(data.get(3, 'Not Found'))
# So it will print 'Not Found' if the value for the key 3 is missing.
# If key 3 has value so it will not print 'Not Found'

print('---------------------')
print('Creating Dictionary with the help of list - ')

# Creating Dictionary with the help of list
keys = ['Navin', 'Kiran', 'Harsh']
values = ['Python', 'Java', 'JS']
# Now merging these two lists into a dictionary
data = zip(keys, values)
# So this data will be a dictionary of combination of key and value pair of these two list.
# Here 'ZIP' will zip these two list: keys and values in to a dictionary Lets see the example below. As here we will use dict as a function for dictionary.
data1 = dict(zip(keys, values))
print('Combining 2 lists to dictionary: ', data1)

# Lets print the key from the dictionary
print('Printing data from dictionary: ', data1['Kiran'])

# Error for the key not present in dictionary
#print('Accessing invalid key from dictionary: ', data1['Monika'])

# Now if you want to add a new value in this data1.
data1['Monika'] = 'CS'
print('Printing data1 after adding new value: ', data1)

# Deleting a key from the dictionary, for this use 'del' keyword
del data1['Harsh']
print('data1 value after deleting item from dictionary - ', data1)

# Moving to advance concepts
# We can have a dictionary as a value in the dictionary itself, same in the list, we can have list as value in the list itself.
# This is something like a nested dictionary or list inside a dictionary.
# Lets create a new dictionary which will have dictionaries and lists inside
prog = {'JS' : 'Atom', 'CS' : 'VS', 'Python' : ['Pycharm', 'Sublime'], 'Java':{'JSE' : 'Netbeans', 'JEE' : 'Eclipse'}}
# So in the above what we have done i trying to put a list inside a dictionary as a value for the key Python and we are also putting a dictionary inside a dictionary for the key Java as a value.
print('Printing new dictionary - ', prog)
# Now testing the above created dictionary
print(prog['JS'])
print(prog['CS'])
print(prog['Python'])
print(prog['Java'])
# You can use the index number with the key to decide which value you want to select.
print(prog['Python'][1])
# You can use the key in dictionary inside the dictionary to access the value
print(prog['Java']['JEE'])

