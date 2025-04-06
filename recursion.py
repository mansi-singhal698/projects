# Recursion: recursion is the process of defining something in terms of itself
def factorial(n):
    if(n == 0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

def fibo(n):
   if(n == 1):
       return 0
   elif(n == 2):
       return 1
   else:
       return fibo(n-1)+fibo(n-2)


print(fibo(5))
