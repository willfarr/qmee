list_to_save = range(100)

f = open ('testout.txt', 'w')
for i in list_to_save:
    f.write(str(i) + '\n')

f.close()