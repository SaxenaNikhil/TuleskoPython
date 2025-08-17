# Printing Patterns
# # # #
# # # #
# # # #
# # # #

for i in range(4):
    for j in range(4):
        print('# ', end='')

    print()

print('# >>>>>>>>>>>>>>')

# New Pattern -
#
# #
# # #
# # # #

for i in range(4): # this is for rows
    for j in range(i+1): # this is for columns, because the value of i starts with 0 so we did i + 1
        print('# ', end='')

    print()

print('# >>>>>>>>>>')

# New Pattern -
# # # #
# # #
# #
#

for i in range(4):
    for j in range(4-i): # Here for each and every i we are reducing the pattern by 1
        print('# ', end='')

    print()