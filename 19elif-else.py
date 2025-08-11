#Elif Else Statement

# CPU -  It has 3 parts which are : Control Unit (CU), Arithmetic/Logic Unit (ALU), Memory unit (MU)

# We have worked with Memory Unit till this time where we were using variables and we were trying to save data.
# ALU - It has two part: Arithmetic Unit, Logic Unit. Arithemtic Unit includes all the addition, subtraction, etc.. and binary conversion.

# Logic Unit - It is basically what makes the computer think. Where we write the code and apply logic to make the computer think. In this we apply condition where we use IF else condition basically.

if True:
    print('Im right')

#else:
    #print('Im wrong!') # This will execute in case if another condition or in case of false condition.

print('#>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Check if the number is odd or even

num = 4
remainder = num % 2
if remainder == 0:
    print("Number is Even")
    if num > 5:
        print('Number is greater than 5')
    else:
        print('Number is smaller than 5')

else:
    print("Number is odd")

print('#>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# if elif else condition

x=5
if x==1:
    print("One")

elif x==2:
    print('Two')

elif x==3:
    print('Three')

elif x==4:
    print('Four')

else:
    print('Wrong Input')