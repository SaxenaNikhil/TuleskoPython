# In-Built Data types in Python
# list of data types are - None, Numeric, List, Tuple, Set, String, Range, Dictionary / Map
# Data types in Numeric are - int, float, complex, bool.
num = 2.5
print('Type of num is - ', type(num))

num = 5
print('Type of num is - ', type(num))

num = 6+9j
print('Type of num is - ', type(num))

a = 5.6
b = int(a)
print('Type of b is - ', type(b))
print('value of b is - ', b)
k = float(b)
print('value of k is - ', k)
k = 6
c = complex(b, k)
print('value of c is - ', c)

print('Check the boolean value for the conditions - ', b < k)
print('Type of expression - ', type(b<k))

print('Integer value of the boolean values - ', int(True))
print('Integer value of the boolean values - ', int(False))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#Other Data types comes under sequence which are - List, Tuple, Set, String, Range
#List
lst = [25, 36, 45, 12]
print('the type of list are - ', type(lst))

#Set
s = {25, 36, 45, 15, 12, 25}
print('Type of set - ', type(s))

#Tuple
t=(25, 36, 4, 57, 12)
print('Type of tuple - ', type(t))

#String
str = "navin"
print('Type of String - ', type(str))

#Range
print('Print range - ', range(10))
# So here we got the range values from 0 to 9
# So we will convert the range into a list so that we can print it
print('Range into a list - ', list(range(10)))
# Moreover list can take more parameters as well
print('range in a list with 3rd parameter', list(range(2, 10, 2))) # This starts with 2 and then gives a gap of 2 nunbers
print('range in a list with 3rd parameter', list(range(2, 10, 3)))

#Dictionary
# It will be in curly brackets because keys should be unique and should not repeat as Set also uses curly brackets and it also does not repeat as well.
d = {'navin':'samsung', 'rahul':'Iphone', 'kiran':'Oneplus'}
print('dictionary - ', d)
# It is a key and value pair
# Get the keys in the dictionary
print('print the keys - ', d.keys())
# Get the values from the dictionary
print('print the values - ', d.values())
# Get the particular value from the dictionary
print('get the values from the dictionary - ', d['rahul'])
print('get the values from the dictionary - ', d.get('kiran'))
