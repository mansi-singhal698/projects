# for loops : for loops can iterate over a sequence of iteratble objects in python. Iterating over a sequence is nothing but iterating over strings,lists,tuples,sets and dictionaries.

# example of string
name = "mansi"
for i in name:
    print(i) 

# example of list
colors = ["red","yellow","blue"]
for color in colors:
    print(color)
    for i in color:
        print(i)

# range()
# What if we do not want to iterate over a sequence?
for k in range(5):
    print(k)

for k in range(1,9):
    print(k)

for k in range(1,12,3):
    print(k)