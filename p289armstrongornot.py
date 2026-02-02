"""
Write a program to input a three digit number. Use a method int Armstrong(int n) to accept the number.
The method returns 1, if the number is Armstrong, otherwise zero(0).
"""

def armstrong(num):
    cnum = num
    s = 0
    while num > 0:
        x = num % 10
        s = s + x ** 3
        num = num // 10

    if s == cnum:
        return 1
    else:
        return 0

num = int(input("Enter a 3 digit number: "))
ans=armstrong(num)
print(ans)