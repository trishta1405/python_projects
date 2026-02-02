num1=int(input("Enter a statring value =>"))
num2=int(input("Enter a ending value =>"))

for i in range(num1,num2+1):
    c=0
    for j in range(2,i):
        if i%j==0:
            c=1
            break
    if c==0:
        print(f"{i} is a prime number")
    else:
        print(f"{i} is divisible by {j}")