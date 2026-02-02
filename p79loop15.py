#2+4+6+8+10

n=int(input("Enter limit =>"))
s=0
for i in range(1,n+1):
    if(n%2==0):
        print(i, end=" + ", )
    s = s + i
print("\n Sum = ", s)