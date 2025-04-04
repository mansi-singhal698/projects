# sets: set is a collection of well-defined objects
s = {2,5,8,8}
print(s)
mansi = set()
print(type(mansi))


# set method
s1 = {1,2,3,4}
s2 = {3,6,7}
print(s1.union(s2) )

print(s1.intersection(s2))
s1.update(s2)
print(s1) #all elements of s1 and s2

s1.intersection_update(s2)
print(s1) #it print common value

s3 = s1.difference(s2)
print(s3)



 
 