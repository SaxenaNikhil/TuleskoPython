# Exercise -
# 1 2 3 4
# 2 3 4
# 3 4
# 4

for i in range(4):
    for j in range(4-i):
        print(j+i+1, end='')

    print()

# Exercise -
# A P Q R
# A B Q R
# A B C R
# A B C D

for row in range(4):
    for col in range(4):
        if(col<=row):
            print(chr(65+col), end=' ')
        elif col == 3:
            print('R', end=' ')
        else:
            print(chr(80+col-1), end=' ')

    print()