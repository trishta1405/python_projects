"""
3. Write a Python program to calculate the product of all items in a list.
Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]
Expected Result: 453752160000
"""

import random
list1=[]
n=int(input("enter the number"))
for i in range(n):
    x=random.randint(-20,20)
    list1.append(x)
print(list1)
m=1
while x in list1:
    m=m*x
print(m)