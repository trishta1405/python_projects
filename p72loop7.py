#20, 1 is odd 2 is even count of both , sum

n=int(input("Enter limit =>"))
c=0
s=0
for i in range(1,n+1):
    if i % 2 == 0:
        print(f"{i} is even")

    else:
        print(f"{i} is odd")
        c=c+1
        s=s+i
print("Count = ",c," Sum = ",s)



