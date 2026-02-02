"""
 Write a Python program to create a new list containing only the first half of elements
from the original list.
Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]
Expected Result: [11, 44, 500, 22] (first 4 elements since 9/2 ≈ 4)
Hint: Use slicing with len(list)//2 to get the first half.
"""

list1=[11, 44, 500, 22, 99, 77, 200, 66, 2]
print(list1)
length=len(list1)
half = length//2

i=0
while i<=half:
    print(list1[i])
    i=i+1
