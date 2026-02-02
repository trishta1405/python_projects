"""
Write a Python program to sum all the items in a list.
Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]
"""

import random
list1=[]
n=int(input("enter the number"))
for i in range(n):
    x=random.randint(-20,20)
    list1.append(x)
print(list1)
print(sum(list1))