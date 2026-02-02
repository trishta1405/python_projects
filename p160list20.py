
#2) search enter 55 , list ?


import random
list1=[]
n=int(input("enter the number"))
for i in range(n):
    x=random.randint(-20,20)
    list1.append(x)
print(list1)
num=int(input("enter the number:"))
if num in list1:
    print(f"{num} is in the list")
else:
    print(f"{num} is not in the list")



