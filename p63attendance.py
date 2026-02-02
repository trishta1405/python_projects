"""
. A student will not be allowed to sit in the exam if his/her attendance is less
than 75%.
Take the following input from the user:
• Number of classes held
• Number of classes attended Print the percentage of classes attended:
• Formula: (Number of classes attended / float(Number of classes held)) * 100
Output: Is the student allowed to sit in the exam or not.
"""

class_held=int(input("please enter the number of classes held: "))
class_attended=int(input("please enter the number of classes attended: "))
percentage=(class_attended / class_held)*100
if percentage>=75:
    print("student allowed to sit in the exam")
else:
    print("student not allowed to sit in the exam")