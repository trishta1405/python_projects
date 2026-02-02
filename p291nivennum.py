"""
Write a program to input a number. Check and display whether it is a Niven number or not. (A number is said to be Niven which is divisible by the sum of its digits).

Example: Sample Input 126
Sum of its digits = 1 + 2 + 6 = 9 and 126 is divisible by 9
"""

num = int(input("Enter a number: "))
s=0
while num>0:
    num=num % 10
    s=s+num
    num=num//10
    s=s+num
if num%s==0:
    print("niven number")
else:
    print("not a niven number")





