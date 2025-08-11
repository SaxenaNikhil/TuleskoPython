# Print all the perfect square number between 1 and 500
for i in range(1, 501):
    if i*i <= 500:
        print(i*i)

# Another way to make this performance efficient would be -
for i in range(1, int(500**0.5)+1):
    print(i*i)

# Here this code - int(500**0.5)+1 is taking the square root of the 500 which basically is 22.something and then adding 1 to it so that we are including the 22 as well as 22*22 would be 484.