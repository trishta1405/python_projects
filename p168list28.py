"""
5. Write a Python program to get the smallest number from a list.
Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]
Expected Result: 2
Hint: Use the min() function to find the smallest number.
"""

import random
list1=[]
n=int(input("enter the number"))
for i in range(n):
    x=random.randint(1,20)
    list1.append(x)
print(list1)
list1.sort()
print(list1)
print(list1[0])