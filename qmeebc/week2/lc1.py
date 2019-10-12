
birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )

#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively. 

# (2) Now do the same using conventional loops (you can choose to do this 
# before 1 !). #

latin = []
for i in birds:
    latin.append(i[0])
print(latin)
# the 0 means it picks just the first

common = []
for i in birds:
    common.append(i[1])
print(common)

weight = []
for i in birds:
    weight.append(i[2])
print(weight)

#these are loops that split them into single lines


latin = [i[0] for i in birds]
print (latin)

#this is the same as the loop but without looping into the empt space
common = [i[1] for i in birds]
print (common)