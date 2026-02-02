"""
 Write a Python program to find common items from two lists.
Sample List 1: [11, 44, 500]
Sample List 2: [77, 44, 11]
Expected Result: [11, 44]
Hint: Use loop to find common elements.
"""

import random
list1=[]
list2=[]
list3=[]
n=int(input("enter the number"))
for i in range(n):
    x=random.randint(1,20)
    list1.append(x)
print(list1)
for i in range(n):
    x=random.randint(1,20)
    list2.append(x)
print(list2)
for x in list1:
    if x in list2 and x not in list3:
        list3.append(x)

print(list3)

