for j in range(12):
    if j % 3 == 0:
        print('hello')
#prints hello 4 times

for j in range(15):
     if j % 5 == 3:
        print('hello')
     elif j % 4 == 3:
        print('hello')

#prints hello 5 times

z = 0
while z != 15:
    print('hello')
    z = z + 3

#also prints hello 5 times

z = 12
while z < 100:
    if z == 31:
        for k in range(7):
            print('hello')
    elif z == 18:
        print('hello')
    z = z + 1

# 8 hellos