# fstring is use for formatting
name = "mansi"
age = 19
print(f"my ame is {{name}} and I am {age} years old")

# Docstrings : Python docstrings are the string literals that appear right after the definition of a function,method,class,or module

def square(n):
    '''Takes in a number n,returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)