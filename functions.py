def larger(a,b):
    if(a>b):
        print(a ,"is greater")
    else:
        print(b,"is greater")

larger(8,9)

def smallest(c,d):
    pass

# Function arguments
# There are four types of arguments that we can provide in a function:
# 1. Default argument
# 2. keyword arguments
# 3. Variable length arguments
# 4. Required Arguments

#default arguments
def average(a=5,b=1):
    print("The average is ",(a+b)/2)

average()

# while creating a function,pass a * before the parameters name while defining the function. The function accesses the arguments by processing them in the form of tuple

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum+i
    print("Average is :",sum/len(numbers))

average(5,6)