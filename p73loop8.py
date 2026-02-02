
#limit , div


n=int(input("Enter limit =>"))
s=0
for i in range(1,n+1):
    if i % div ==0:
        print(i)
        s=s
print("div = ",s)