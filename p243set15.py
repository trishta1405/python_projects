#Write a Python program to find the symmetric difference between two sets.

s1 = {11, 22, 33, 44, 55}
s2 = {11, 22, 99, 66, 55}
s3=s1-s2
s4=s2-s1
for x in s4:
    s3.add(x)
print(s3)
