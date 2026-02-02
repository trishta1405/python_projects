import random

correct=0
incorrect=0
print("print 1 for addition")
print("print 2 for subtraction")
print("print 3 for multiplication")
print("print 4 for division")
user_input=int(input("Enter to choose:"))
"""import random
for i in range(1,6):
    x=random.randint(1,50)
    y=random.randint(1,50)
    print(x)
    print(y)"""
if user_input==1:
    for i in range(1, 6):
        x = random.randint(1, 50)
        y = random.randint(1, 50)
        print(x)
        print(y)
        add = x + y
        num = int(input("enter the addition of numbers:"))
        if num == add:
            print("your answer is correct")
            correct = correct + 1
        else:
            print("your answer is incorrect")
            incorrect = incorrect + 1
elif user_input==2:

    for i in range(1, 6):
        x = random.randint(1, 50)
        y = random.randint(1, 50)
        print(x)
        print(y)
        add = x + y
        num = int(input("enter the addition of numbers:"))
        if num == add:
            print("your answer is correct")
            correct = correct + 1
        else:
            print("your answer is incorrect")
            incorrect = incorrect + 1
elif user_input==3:

    for i in range(1, 6):
        x = random.randint(1, 50)
        y = random.randint(1, 50)
        print(x)
        print(y)
        add = x + y
        num = int(input("enter the addition of numbers:"))
        if num == add:
            print("your answer is correct")
            correct = correct + 1
        else:
            print("your answer is incorrect")
            incorrect = incorrect + 1
print(f"you gave {correct} correct answer")
print(f"you gave {incorrect} incorrect answer")