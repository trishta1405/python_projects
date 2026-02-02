"""
 Write a Python program to remove a key from a dictionary.
Sample data:
Enter key to delete: rahul
Expected Output:
marks = {"ram": 33, "devesh": 30, "jayul": 34, "jiya": 16, "sadhana": 11, "meena": 19}
Hint: Use the del statement or the pop() method to remove the key from the dictionary.
"""

marks = {
"ram": 33,
"rahul": 15,
"devesh": 30,
"jayul": 34,
"jiya": 16,
"sadhana": 11,
"meena": 19
}
key=input("Enter key to delete: ")
if key in marks:
    del marks[key]
print(marks)