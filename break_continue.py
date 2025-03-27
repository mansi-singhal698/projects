# break statement : the brake statement enables a program to skip over a part of the code. A break statement terminates the loop it lies within.

for i in range(12):
    if(i == 4):
        break
    print("5 X",i+1,"=",5*(i+1))

print("outside the loop")

# continue statement : it is use for skipthe iteration

for i in range(12):
    if(i == 4):
        continue
    print("5 X",i+1,"=",5*(i+1))
