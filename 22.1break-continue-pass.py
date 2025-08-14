# Break, Continue and Pass -

# Continue will skip the remaining statement and will go back to the next iteration. So it will skip only the particular iteration.
for i in range(5):
    if i == 3:
        continue # So here at i == 3 it will skip the remaining iteration.
    print("Hello", i)

print('# >>>>>>>>>>>>>>>')
# >>>>>>>>>>>>>>>
# Break - The moment you see i == 3 at break statement it will break that loop, so it will not continue with the loop. So after i == 2 it will not print anything and even the remaining iteration will also not work in that scenario. Here the entire loop gets break.
for i in range(5):
    if i == 3:
        break
    print('Hello Break', i)


print('# >>>>>>>>>>>>>>')
# >>>>>>>>>>>>>>
# Pass - In the scenario when you don't know what logic you want inside a loop or a function or anything then in that case if you just want to keep it empty and things to fill in later as the logic strikes, then just use 'pass' to make things work.
# Pass will skip the function or the logic or block

def fun():
    print('inside function')
    pass
    print('inside function2')

fun()

print('# >>>>>>>>>>>')

for i in range(5):
    if i == 4:
        pass
    print('Hello Pass', i)
