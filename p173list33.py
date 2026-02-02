"""
. Write a Python program to remove even numbers from a list.
Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]
Expected Result: [11,99, 77, 11]
"""

import random
list1=[]
list2=[]
n=int(input("enter the number"))
for i in range(n):
    x=random.randint(1,20)
    list1.append(x)
if x % 2 == 0:
        list2.append(x)
print(list1)
print(list2)