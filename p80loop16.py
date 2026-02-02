#1+3+5+7+9+11

n=int(input("Enter limit =>"))
s=0
for i in range(1,n+1):
    if i %2 ==1:
        print(i,end=" + ",)
        s = s + i
print("\n Sum = ", s)





