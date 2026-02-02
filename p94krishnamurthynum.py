num=int(input("Enter a number:"))
y=num
sum=0
while y>0:
    rem=y%10
    f=1
    for i in range(1, rem+ 1):
        f=f*i
    sum=sum+f
    y=y//10
if sum==num:
    print("Krishnamurthy Number")
else:
    print("Not a Krishnamurthy Number")


