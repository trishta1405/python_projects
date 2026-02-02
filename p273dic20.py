
import random
d1={}
n=int(input("Enter range =>"))
c=0
for i in range(1,n+1):
    k=i
    v1=random.randint(1,50)
    v2=random.randint(1,50)
    v3=random.randint(1,50)
    d1[i]=[v1,v2,v3]
print(d1)
for k, marks in d1.items():
    if marks[0] <= 18 and marks[1] <= 18 and marks[2] <= 18:
        print("Student",k,"fail", marks)
        c=c+ 1
print("fail students =",c)