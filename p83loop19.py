#1+ 8 + 27 + 64 + 125 +

n=int(input("Enter limit =>"))
s=0
for i in range(1,n+1):
    ans=i*i*i
    print(ans,end=" + ")
    s = s + ans
print("\n Sum = ", s)