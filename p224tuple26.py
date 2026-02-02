# Write a Python program to multiply all elements in a tuple by 2.

t1=(11,34,56,4,33,667,32,89,11,11,11)
l1=list(t1)
for x in l1:
    l1.append(x*2)
t1=tuple(l1)
print(t1)
