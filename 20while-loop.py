# While loop -
# Execute the loop for 5 times

# counter initialise
i = 1
while i<=5: # Condition Check
    print('Tulesko', i)
    i = i + 1 # Increment the value here inside the while loop

print('# >>>>>>>>>>>>>>')

# Another way to solve the same while decrementing would be
a = 5
while a>=1:
    print('Tulesko', a)
    a = a - 1 # Decrement the value here.

print('# >>>>>>>>>>>>>')

# Print the nested while loop
b=1
while b<=5:
    print('Tulesko', b, ' ', end="") # This end="" will make sure that it stays on the same line and do not go to the new line. So Rocks will stay with Tulesko
    c = 1 # Initialisation for inner while loop
    while c<=4:
        print('Rocks', c, ' ', end="") # Here with end="" Rocks will stay with other Rocks in the same line.
        c=c+1

    b=b+1 # This one executes for the outer while loop
    print() # This print will make sure that the outer loop which is Tulesko one will separate the other statement for another outer loop.