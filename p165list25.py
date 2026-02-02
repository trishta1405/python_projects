#7) value enter delete list

import random
list1=[]
n=int(input("enter the number"))
for i in range(n):
    x=random.randint(-20,20)
    list1.append(x)
print(list1)
num=int(input("enter the number"))
while num in list1:
    list1.remove(num)
print(list1)