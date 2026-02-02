#Print Sum of even and Count also
c=0
sum=0
t1=(12,43,56,22,78,34)
for x in t1:
    if x%2==0:
        print(x)
        c=c+1
        sum=sum+x

print("sum:",sum)
print(f"count={c}")