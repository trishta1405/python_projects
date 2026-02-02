num=int(input("enter a number: "))
sum=0
y=num
while num>0:
    rem=num%10
    sum=sum+rem*rem*rem
    num=num//10
if y==sum:
    print(f"{y} is armstrong number")
else:
    print(f"{y} is not armstrong number")