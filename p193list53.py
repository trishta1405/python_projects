import random
list1=[]
list3=[]
n=int(input("enter the number"))
for i in range(n):
    x=random.randint(0,20)
    list1.append(x)
print(list1)
list2=[]
for i in range(n):
    x=random.randint(0,20)
    list2.append(x)
print(list2)
for x in list1:
    if x not in list2:
        list3.append(x)
print(list3)