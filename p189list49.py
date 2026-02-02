"""
Write a Python program to find the average of all numbers in a list.
Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]
Expected Result: 113.44 (sum = 1021, count = 9, 1021/9 ≈ 113.44)
Hint: Use sum() and len() to calculate the average (sum/length)
"""

list1 = [11, 44, 500, 22, 99, 77, 200, 66, 2]
total=sum(list1)
c=len(list1)
average = total/c
print("average:", round(average, 2))
