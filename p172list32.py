"""
12. Write a Python program to clone or copy a list.
Sample List: [11, 44, 500]
Expected Result: [11, 44, 500]
"""

import random
list1=[]
list2=[]
n=int(input("enter the number"))
for i in range(n):
    x=random.randint(1,20)
    list1.append(x)
print(list1)

list2.append(list1)
print(list2)