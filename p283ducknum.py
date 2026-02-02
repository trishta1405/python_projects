num=int(input("enter a number:"))
y=num
c=0
while num > 0:
    rem = num % 10
    if rem==0:
        c=1
        break
    num = num // 10

if c == 1:
    print("It is a Duck Number")
else:
    print("It is not a Duck Number")