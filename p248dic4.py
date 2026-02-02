"""
Write a Python script to print data in vertical form and display whether that student is
pass or fail from the dictionary. (18 marks to pass)

Hint: Use a loop and a conditional statement to determine if each student passed or failed.
"""

marks = {
"ram": 33,
"rahul": 15,
"devesh": 30,
"jayul": 34,
"jiya": 16,
"sadhana": 11,
"meena": 19,
"karan": 20
}
for k, v in marks.items():
    if v>=18:
        print(k,v,"passed")
    else:
        print(k,v,"failed")