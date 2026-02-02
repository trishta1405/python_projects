"""
 Write a Python program to update a dictionary with new student marks.
Sample data:
"""
marks = {
"ram": 33,
"rahul": 45
}
name=input("Enter student name: ")
mark=int(input("Enter marks: "))
marks[name]=mark
print(marks)
