"""
Write a program to accept a number and check whether it is a Spy number.
 (A number whose digit sum equals digit product. Example: 112 → 1+1+2 = 1×1×2)
"""
num=int(input("Enter a number: "))
c=0
s=1
while num>0:
    digit =num% 10
    c=c+digit
    s=s*digit
    num=num//10

if c==s:
    print("spy number")
else:
    print("not a spy number")
