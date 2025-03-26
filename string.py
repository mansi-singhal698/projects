a = "mansi"
b = 'mansi'
print(a)
print(a[0]) # in python string is like an arrray of characters

#for loop is use to print the whole string
for ch in a:
    print(ch)

# we can find the length of a string using len() function
fruit = "mango"
len1 = len(fruit)
print(len1)


# slicing
print(fruit[0:5])
print(fruit[:5])
print(fruit[0:])

# it means len(fruit)- 2
print(fruit[0:-2]) 

# String method
# 1st method upper()
str1 = "mansi"
print(str1.upper())

# 2nd method
str1 = "mansi!!!!!!!!!!!!!"
print(str1.lower())

# 3rd method
print(str1.rstrip("!"))

# 4th method
print(str1.replace("mansi","deepali"))

# 5th method
cap = str1.capitalize()
print(cap)

# 6th method
print(str1.endswith("!!!!!!!!"))