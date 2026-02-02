#-1+2-3+4-5

n=int(input("Enter limit =>"))
s=0
for i in range(1,n+1):
    if(i%2!=0):
        ans=-i
        print(ans,end=" + ")
    else:
        print(i,end=" + ")
        s = s + ans
print("\n Sum = ", s)