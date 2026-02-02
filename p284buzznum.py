#divisible by 7 or contains 7

num=int(input("enter a number:"))
y=num
c=0
while num > 0:
    rem = num % 10
    rem2=num % 7
    if rem==7:
        c=+1
    elif rem2==0:
        c=+1
    break

if c==1:
    print("It is a buzz number")
else:
    print("It is not a buzz number")