#Display only numbers divisible by 7 , count and sum it

c=0
sum=0
t1=(12,43,56,22,78,34,28,34,54,21)
for x in t1:
    if x%7==0:
        print(x)
        c=c+1
        sum=sum+x

print("sum:",sum)
print(f"count={c}")