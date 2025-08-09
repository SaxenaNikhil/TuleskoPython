# Lists
nums = [25, 12, 36, 95, 14]
print(nums)

# lets get the values from the lists
print(nums[0])
print(nums[4])

print('-------------------')

# Getting the values from the middle of the lists
print(nums[2:])

print('-------------------')

# Accessing the values from the list using the negative range
print(nums[-1])
print(nums[-5])

print('-------------------')

# list can contain any type of data
names = ['navin', 'kiran', 'john']
print(names)

values = [9.5, 'Navin', 25]
print(values)

print('-------------------')

# Now two list working together inside a list
mil = [nums, names]
print('Combining two lists inside a list - ', mil)

print('-------------------')

# Note - List are mutable which basically means that you can change the values.
# Performing functions on the list

# Append function on the nums
print('Value of Nums before append - ', nums)
nums.append(45) # It will append in the end of the list
print('Value of Nums after append - ', nums)

# Insert function on the nums
# This means insert the value in the between of the list
nums.insert(2, 77) # At Index 2 this will insert the value 77 to list
print('Value of Nums after Insert - ', nums)

# Now to remove the element from the list, pass the element value which you want to remove
nums.remove(14) # This will remove the value 14 from the list
print('Value of Nums after Remove - ', nums)

# Now to remove the element from the list using the index number
nums.pop(1) # This will remove the element at index 1 which is second element in the list i.e. 12
print('Value of Nums after pop - ', nums)
# Now if you don't mention the index in the pop function then it will remove the last element in the list
nums.pop() # This will remove the last element in the list i.e. 45
print('Value of Nums after pop without index value - ', nums)

# Now to delete multiple values from the list, we will use 'del' keyword
del nums[2:] # This will delete the elements from the list starting from index 2 till the end
print('Value of Nums after del - ', nums)

# Now using extend function to add multiple values to the list
nums.extend([29, 12, 14, 36])
print(nums)

print('-------------------')

# Performing some in-build functions on list
print('Performing some in-build function on list')
# get the min value
print('min value - ', min(nums))

# get the max value
print('max value - ', max(nums))

# get the sum
print('sum of all value - ', sum(nums))

# Sort the value in the list
nums.sort()
print('sorted values of nums - ', nums)