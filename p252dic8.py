"""
 Write a Python program to count the number of students who passed (marks >= 18)
in the dictionary.
"""

c=0
marks = {
"ram": 33,
"rahul": 15,
"devesh": 30,
"jayul": 34,
"jiya": 16,
"sadhana": 11,
"meena": 19,
"karan": 20,
"anita": 25
}
for value in marks:
    if marks[value] >= 18:
        c=c+1
print("Number of passed students:",c)