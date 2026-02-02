import random
list1=[]
list2=[]
n=int(input("enter the number"))
for i in range(n):
    x=random.randint(-20,20)
    list1.append(x)
    if x%2==0:
        list2.append(x)

print(list1)
print(list2)