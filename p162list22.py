#4) pos -neg , neg -pos list2 add

import random
list1=[]
list2=[]
n=int(input("enter the number"))
for i in range(n):
    x=random.randint(-20,20)
    list1.append(x)
print(list1)
result = [-x for x in list1]
list2.append(result)
print(list2)
