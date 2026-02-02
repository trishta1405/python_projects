"""
6. Write a Python program to add the first and last value of the list.
Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]
Expected Result: 13
Hint: Access the first value using list[0] and the last value using list[-1], then add them.
"""

import random
list1=[]
n=int(input("enter the number"))
for i in range(n):
    x=random.randint(1,20)
    list1.append(x)
print(list1)
add=list1[0]+list1[-1]
print(add)