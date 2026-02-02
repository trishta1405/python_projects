correct=0
incorrect=0
import random
for i in range(1,6):
    x=random.randint(1,50)
    y=random.randint(1,50)
    print(x)
    print(y)
    add=x+y
    num=int(input("enter the addition of numbers:"))
    if num==add:
        print("your answer is correct")
        correct=correct+1
    else:
        print("your answer is incorrect")
        incorrect=incorrect+1
print(f"you gave {correct} correct answer")
print(f"you gave {incorrect} incorrect answer")