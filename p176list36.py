"""
21. Write a Python program to square each element in a list.
Sample List: [11, 2, 4, 3, 6, 7]
Expected Result: [121, 4, 16, 9, 36, 49]
Hint: Use a loop or list comprehension to square each number using number ** 2.
"""
list2=[]
list1=[11, 2, 4, 3, 6, 7]
print(list1)
for x in list1:
    list2.append(x**2)
print(list2)