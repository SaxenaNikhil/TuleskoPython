# Exercise -
# Write a code to print all the values from 1 to 100. Skip the numbers which are divisible by 3 or 5.

#num = 1
#while num<=100:
    #if num%3 == 0 or num%5 == 0:
        #num += 1 # Increment before skipping
        #continue
    #print(num)

    #num=num+1

#print('# >>>>>>>>>>>>>>>')

# >>>>>>>>>>>>>>>>>>>>>>>

num = 1
while num<=100:
    if not (num%3 == 0 or num%5 == 0): # This will skip number divisible 3 and 5
        print(num)
    num = num + 1

print('# >>>>>>>>>>>>>>>>>')

# Write a code to print below pattern.
# # # # #
# # # # #
# # # # #
# # # # #

i = 1
while i<=4: # Outer loop for 4 times as this is for rows
    j = 1
    while j<=5: # Inner loop for 5 times as this is for columns
        print('#', ' ', end="") # Used end="" so that the print statement does not go in the next line
        j = j + 1 # Increment for inner loop

    print()
    i = i + 1 # Increment for outer loop