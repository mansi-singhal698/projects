# tuple is immutable

tup = (1,2,3,7,8,2,5,60)
print(tup)
print(tup[0])
for i in tup:
    print(i)

print(tup[1:7]) #slicing

#tuple methods
print(tup.count(2))

print(len(tup))


