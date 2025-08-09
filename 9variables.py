# Variables
# this variable num has value 5 and the address in the internal memory where this is stored.
num = 5
# Now to get the address of variable num
print(id(num))

# lets check the same for another concept
name = 'navin'
print(id(name))


# In python if both variables are assigned the same data here which is a is 10 and b is assigned the variable a, then both will point to the same 'box' and will not be getting boxes for each variable and that's why python is memory efficient
a = 10
b = a
print('value of a - ', a)
print('value of b - ', b)
print('id of a - ', id(a))
print('id of b - ', id(b))
print('id of 10 - ', id(10))
# Note the address is not based on the variable name but rather its based on the box itself.
# but if we assign the k variable the value 10, then k also points to the same. Its because we are not talking about k here but rather we are talking about value 10 because indirectly your k is referring to 10.
# Moreover these variables are also called tags because we are tagging them so 10 is a value and we are tagging a, b, k variables, so everything is tagging to the same object.
k = 10
print('id of k - ', id(k))
# Due to which k will also get the same id as others as they all are pointing to the value 10.

# Now lets update the value for a and see the response.
a = 9
print('value of a again with new value - ', id(a))
# So the id of a will be different because we got different box which has different address as it has different value for a
# Now lets see if it updates the id of b as b = a in the last statement.
print('id of b check - ', id(b))
# The id of b refers to the old value of a because it was pointing to a with older value.

# Now if we update the value of k, so it will point to the box 9
k = a
print('id of k check - ', id(k))
# Here the id of k is updated to the new value.

# Now if b point to another box with value such as 8.
# Then we will have 3 boxes in total now which are 8,9,10. So here a and k are pointing to 9 and b is pointing to 8 so nothing is pointing to box with value 10. Now 10 is dead in memory and no one is using it.
# So the variable which is not in use and is not tagged by any variable so it will be garbage collected later.

# Creating a constant which is it cannot change the value or is immutable. But in python we cannot do that.

# Concept: Type of the varialbe.
PI = 3.14
print('Value of PI - ', PI)
print('Type of variable - ', type(PI))
# Note each variables has a type which is in-built type.
# Note - You can also create your own type as well.
