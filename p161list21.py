#enter 55 greater value

import random
list1=[]
n=int(input("enter the number"))
for i in range(n):
    x=random.randint(-20,20)
    list1.append(x)
print(list1)
num=int(input("enter the number:"))
for x in list1:
    if num<x:
        print(x)
