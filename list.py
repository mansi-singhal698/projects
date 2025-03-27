list1 = [3,5,6,"mansi",True]
print(list1)
print(list1[0])
print(list1[-3])

# check whether an item in present in the list?
# We can check if a given item is present in the list. This is done using the in keyword.

if 6 in list1:
    print("6 is present")
else:
    print("6 is not present")


# list method
l = [1,2,4,3,5]
l.append(7)
print(l)
l.sort()
print(l)
l.pop() 
print(l)
l.remove(3)
print(l)
