# For else Concept

nums = [10, 12, 16, 18, 21, 26, 25]

# This code down here will print all the numbers which are divisible by 5.
for num in nums:
    if num % 5 == 0:
        print(num)

print('# >>>>>>>>>>>>>>>>>>')

# Concept 2
# This will print the first number only which is divisible by 5 and will not check for another number from the list.
nums1 = [10, 12, 16, 18, 21, 26, 25]
for num in nums1:
    if num % 5 == 0:
        print(num)
        break

print('# >>>>>>>>>>>>>>>>>>')

# Concept 3
# Now lets say we don't have any number divisible by 5 then what to do?
# So we use for-else concept but we want the else condition to execute once all of the iteration is done then it executes the else condition for for-loop.
# break in if block is mandatory for for-else loop
nums2 = [12, 16, 18, 21, 26]
for num in nums2:
    if num % 5 == 0:
        print(num)
        break # this is compulsory for for-else condition
else:
    print('not found')