#hindi heighest

import random

d1 = {}
n = int(input("Enter range => "))

t=0
c=0

highest_v3 = 0
top_v3_student = 0

for i in range(1, n+1):
    v1 = random.randint(1, 50)
    v2 = random.randint(1, 50)
    v3 = random.randint(1, 50)
    d1[i] = [v1, v2, v3]

print(d1)


for k, v in d1.items():
    total=v[0]+v[1]+v[2]

    if v[0]>=18 and v[1]>=18 and v[2] >= 18:
        print("Student",k,"pass",v,"Total =", total)
        t+= 1
    else:
        print("Student", k, "fail",v,"Total =", total)
        c+= 1

    if v[2] > highest_v3:
        highest_v3 = v[2]
        top_v3_student = k

print("total passed students =", t)
print("total failed students =", c)
print("top student in Maths =", top_v3_student)