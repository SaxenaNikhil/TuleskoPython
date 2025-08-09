# Bitwise
# We have 6 different operators - Complement(~), And(&), Or(|), XOR(^), Left Shift(<<), Right Shift(>>)

# Complement Operator(~), here this sign ~ is called tilde. So we say it as tilde sign.
# Here Complement means it will simply do the reverse of the binary numbers such as 0 to 1 and 1 to 0.
# This will print -13 because the binary format for this 12 is 0b1100 which is basically 00001100 and now to find the complement of 12 which is ~12 so we have to reverse the number given above, which will be 11110011 which is basically -13.
print(bin(12))
print(~12)
# So basically we have a concept of 2's complement due to which we can store positive numbers in the system only. So how do we store the negative numbers in the system? So to store -13 in the system we need to convert it to positive number with the help of 2's complement and to find it we need to find (1's complement + 1)
print(bin(13))
# So to find it we have to convert the binary format of 13 which is '00001101' and find the 1's complement of this + 1 which is 11110011. which is basically -13 and also in binary there are 8 bits so that's why there are 8 digit binary number.

# AND Operator - In this Operator only 1 1 is 1 and rest all is 0.
print(12 & 13)
# Why 12? 12 is '00001100' and 13 is '00001101' so doing the AND operator between these two will give - '00001100' which is basically 12.

print(25 & 30)
# 25 is '00011001' and 30 is '00011110' Output should be '00011000' which is basically 24.

# OR Operator - In this operator if you find 1 then you get 1 so in all of the case you will get 1 but in 0 0 you get 0.
print(12 | 13)
# Output should be 13 as for 1 you get 1 back - '00001101'

# XOR Operator - For odd number of 1 you get 1 so basically in this if both the numbers are different then you get 1 otherwise you get 0.
print(12 ^ 13)
# Here the output is 1 its because 12 is '00001100' and 13 is '00001101' so basically for same number its 0 and for different number its 1. Output comes out to be '00000001'

# Left Shift - Here we move the numbers to the left and dot to the right.
print(10 << 2)
# Here the output is 40 why? Because 10 binary is '00001010' and now we have to apply the left shift here on this so it will be like we will be moving a dot(.) to right because we will be moving the bits to the left by 2 as that is left shift 2 so the binary will become '101000' so on this we will go with the number calculation which will be from left 2^0 to the right 2^5 and we will ignore the zeros here in this one. so we will add only the one's here. which will be 2^3 + 2^5 = '40' which is basically 40.

# Right Shift - So in right shift you loose bits compared to the left shift where you gain bits. So in right shift we move the bits on the right side and dot(.) to the left side.
print(10 >> 2)
# So here the binary for 10 is - '00001010' and now we have to apply right shift here on this one we will move the 2 bits to the right or we can say like we will be moving dot 2 positions to the left. So it will come-out to be '00000010' which is basically 2^1 = 2. Which means that on considering only the ones will give me the value of 2.
