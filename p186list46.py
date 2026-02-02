"""
Write a Python program to find the sum of all numbers divisible by 3 in a list.
Sample List: [11, 12, 15, 22, 99, 77, 200, 66, 2]
Expected Result: 192 (12 + 15 + 99 + 66 = 192)
Sample List 1: [11, 44, 500, 22]
Sample List 2: [11, -44, 500, 22]
Hint: Use a loop and the modulus operator % to check divisibility by 3, then add those
numbers.
"""
list2=[]
list1=[11, 12, 15, 22, 99, 77, 200, 66, 2]
print(list1)
for x in list1:
    if x % 3 == 0:
        list2.append(x)
print(sum(list2))
