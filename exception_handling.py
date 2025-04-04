a = int(input("enter the number :"))
print(f"multiplication table of {a} is :")

try:
    for i in range(1,11):
        print(f"{a}*{i} = {a*i}")
except:
    print("invalid input")