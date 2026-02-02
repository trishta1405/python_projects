#2 pass , count


import random
d1={}
n=int(input("Enter range =>"))
t=0

for i in range(1,n+1):
    k=i
    v1=random.randint(1,50)
    v2=random.randint(1,50)
    v3=random.randint(1,50)
    d1[i]=[v1,v2,v3]
print(d1)
for k, v in d1.items():
    if v[0] >= 18 and v[1] >= 18 and v[2] >= 18:
        print("Student",k,"pass",marks)
        t=t+1
print("passsed students =",t)

