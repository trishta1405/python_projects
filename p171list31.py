"""
 Write a Python program to check if a list is empty and display the total number of
elements.
Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]
Expected Result: There are 11 elements
Hint: Use the len() function to find the number of elements, and check if len(list) == 0
to determine if it's empty.
"""

list1=[11, 44, 500, 22, 99, 77, 200, 66, 2, 11,22 ]
print(list1)
print(len(list1))
if len(list1) == 0:
    print("The list is empty")
else:
    print("The list not is empty")