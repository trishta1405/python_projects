#Magic number: A Magic number is a number in which the eventual sum of the digit is equal to 1.For example: 28 = 2+8=10= 1+0=1

sum=0
num=int(input("Enter a number:"))
while num>0:
    x=num%10
    sum=sum+x
    num=num//10
num = sum
print(num)
sum = 0
while num > 0:
    x=num%10
    sum=sum+x
    num = num // 10
if sum == 1:
    print("Magic Number")
else:
    print("Not a Magic Number")

