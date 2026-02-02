
import random
d1={}
n=int(input("Enter range =>"))
for i in range(1,n+1):
    k=i
    v1=random.randint(1,50)
    v2=random.randint(1,50)
    v3=random.randint(1,50)
    d1[k]=[v1,v2,v3]
print(d1)
ch=int(input("Enter a roll num:"))
if ch in d1:
    print(d1[ch])
else:
    print("sorry")
