#1 + 4 + 9 + 16 + 25 +

n=int(input("Enter limit =>"))
s=0
for i in range(1,n+1):
    ans=i*i
    print(ans,end=" + ")
    s = s + i
print( "\n Sum = ", s)