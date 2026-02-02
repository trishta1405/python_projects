#1 + 4+ 27 + 16 + 125 +

n=int(input("Enter limit =>"))
for i in range(1,n+1):
    if(n%2==0):
        ans=i*i
    else:
        ans=i*i*i
    print(ans,end=" + ",)