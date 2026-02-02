num=int(input("enter a number: "))
rev=0
y=num
while num>0:
    rem=num%10
    rev=(rev * 10)+rem
    num=num//10
if y==rev:
    print(f"{y} is palindrome number")
else:
    print(f"{y} is not palindrome number")

