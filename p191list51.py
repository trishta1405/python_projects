import random
list1=[]
list2=[]
n=int(input("enter the number"))
for i in range(n):
    x=random.randint(0,20)
    list1.append(x)
print(list1)
for x in list1:
    for i in range(2,x):
        c=0
        if x%i==0:
            c=1
            break
        if c==0:
            list2.append(x)
            break
print(list2)


