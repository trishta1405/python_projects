import random
list1=[]
n=int(input("enter the number"))
for i in range(n):
    x=random.randint(-20,20)
    list1.append(x)
print(list1)
c=0
t=0
for x  in list1:
    if x>=1:
        print(f"{x} is positive")
        c=c+1
    else:
        print(f"{x} number is negative")
        t=t+1
print("the number of positive numbers is",c)
print("the number of negative numbers is",t)
