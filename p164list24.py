#6) 2 list common values print

import random
list1=[]
list2=[]
n=int(input("enter the number"))
for i in range(n):
    x=random.randint(-20,20)
    list1.append(x)
    x=random.randint(-20,20)
    list2.append(x)
print(list1)
print(list2)

for x in list1:
    if x in list2:
        print(x)
