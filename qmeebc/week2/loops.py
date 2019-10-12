# FOR loops in Python
for i in range(5):
    print(i)
#just prints the list of numbers in range

my_list = [0, 2, "geronimo!", 3.0, True, False]
for k in my_list:
    print(k)
#prints my_list as a vertical list


total = 0
summands = [0, 1, 11, 111, 1111]
for s in summands:
    total = total + s
    print(total)
#check this one


# WHILE loops  in Python
z = 0
while z < 100:
    z = z + 1
    print(z)
#lists 1-100, maybe "adds 1 every time z is under 100"?


b = True
while b:
    print("GERONIMO! infinite loop! ctrl+c to stop!")
# ctrl + c to stop!
#starts an endless loop
