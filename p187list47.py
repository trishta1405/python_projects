"""
38. Write a Python program to check if all elements in a list are positive.
Expected Result: True for first list, False for second list
ample List 1: [11, 44, 500, 22]
Sample List 2: [11, -44, 500, 22]
Hint: Use a len() and count=count+1
"""
list1= [11, 44, 500, 22]
list2= [11, -44, 500, 22]
print(list1)
print(list2)
c=0
for x in list1:
    if x > 0:
        c=c+1

if len(list1) ==c:
    print("true")
else:
    print("false")

c=0
for x in list2:
    if x > 0:
        c = c + 1

if len(list2) == c:
    print("true")
else:
    print("false")
