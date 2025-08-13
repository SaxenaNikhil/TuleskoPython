#x = int(input("How many Candies do you want? "))

#i = 1
#while i<=x:
    #print("Candy")
    #i+=1

# >>>>>>>>>>>>>>>>>
# Break -
# User - I want n number of candies, now if the number matches or lower to available candies then its okay otherwise its not.

av = 5 # These are number of available candies.
y = int(input("How many Candies you want? ")) # User input for candies he need

i = 1
while i<=y:
    if i>av:
        print('Out of Stock!')
        break # This break statement broke the if loop where the entire loop got terminated

    print('Candy') # This statement is a part of while loop and not if loop
    i+=1

print("Bye") # This statement is after the while loop

print('# >>>>>>>>>>>>>>>>>>>')

# >>>>>>>>>>>>>>>>>
# Continue -
# Print the number from 1 to 100 which and skip those which are divisible by 3 or 5

for i in range(1, 101):
    if i%3==0 or i%5==0:
        continue # This will skip the numbers which are divisible by 3 or 5
    print(i)

print('Bye')

print('# >>>>>>>>>>>>>>>')

# Print the number from 1 to 100 which and skip those which are divisible by both 3 and 5. Such as 15 will not be there as 15 is divisible by both 3 and 5.

for i in range(1, 101):
    if i%3==0 and i%5==0:
        continue # This will skip the numbers which are divisible by both 3 and 5
    print(i)

print('Bye')

print('# >>>>>>>>>>>>>>>')

# >>>>>>>>>>>>>>>>
# Pass -
# Example -  I want to print all the values from 1 to 100 but leaving the values which are odd number.

for i in range(1, 101):
    if(i%2!=0): # Check for odd numbers
        pass # It means there is no code so just ignore it. Since we have nothing to put in the condition so rather than leaving an empty if block we will just pass.
    else:
        print(i)

print('Bye')