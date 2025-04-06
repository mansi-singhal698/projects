# The enumerate function is a built-in function in Python that allows you to loop over a sequence and get the index and value of each element in the sequence at the same time.

fruits = ['apple','banana','mango']
for index,fruit in enumerate(fruits):
    print(index,fruit)


fruits = ['apple','banana','mango']
for fruit in fruits:
    print(fruit) #it give only value not index 