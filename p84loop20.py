#1 + 4+ 27 + 16 + 125 +

n=int(input("Enter limit =>"))
s=0
for i in range(1,n+1):
    if(n%2==0):
        ans=i*i
    else:
        ans=i*i*i
    print(ans,end=" + ",)
    s = s + ans
print("\n Sum = ", s)