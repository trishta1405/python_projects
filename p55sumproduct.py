"""
Given two integer numbers, return their product only if the product is equal
to or lower than 50; else, return their sum.
"""

num1=int(input("please enter the first number:"))
num2=int(input("please enter the second number:"))

sum=num1+num2

if sum<=50:
    print("The product is equal:",sum)
else:
    print("The product is equal:",num1*num2)