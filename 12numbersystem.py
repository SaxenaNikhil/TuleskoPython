# Python with Tulesko

# Number System
# Binary, Decimal, Octal, Hexadecimal

# To convert the number 25 to binary format
# Using bin() function we can convert the number from decimal system to binary system
# Now in 'Decimal system' the 'base is 10' and in 'binary system' the 'base is 2' which means in decimal system we can go from 0 to 9 so we have 10 digits but in binary system we can go from 0 to 1 so we have 2 digits so thats why we say it as bits which is basically binary digits.

# In 'Octal System' we have 'base 8' from 0 to 7 and in 'Hexadecimal' we have 'base 16' which goes from '0 to 9 and after 9 it goes from a to f' so in total we have 16.

# 25 number to binary format
print(bin(25))
# In this the output is 0b11001 so how do we come upto this, if we divide the number 25 by 2 and we only take into account the remainder of these then we will come to this.. so the remainder comes upto be 10011 this is when 25 is divided by 2 and then 12 is divided by 2 and so on until the last 1 is left. Now we will reverse this number so it will be 11001 and for binary number we will put the 0b in front of this number. Which will come out to be 0b11001. Because 0b identifies that this number is a binary format.

print(0b0101) # which is basically number 5 as it will give the output in decimal format.

# To convert number 25 to Octal format.
print(oct(25))
# 0o31 is the octal format for 25. Where '0o' tells its octal

# To convert number 25 to Hex format.
print(hex(25))
# 0x19 is the hexadecimal format for 25. Where '0x' tells its hexadecimal
print(hex(10))
# 0xa tells its a 10 as after 0 to 9 it goes to alphabets which is a to f and a indicates 10
print(0xf) # This is basically 15 from a to f its 15 as a is 10

# Find binary format for 31, 52, 65 or find the decimal format for this binary - 0b110011010 so start from the last of the binary digit as 2^0, 2^1, towards the left and dont focus on the 0 bits and leave them, now only add those 1 bits 2 power to get the decimal number.