num=int(input("enter a number:"))
sum=0
i=1
while num>i:
    if num%i==0:
        sum=sum+i
    i=i+1
if sum==num:
    print("it is a perfect number")
else:
    print("it is not a perfect number")