# Write a Python program to merge two tuples.

t1=(12,34,56,77,54,335,88,9,66)
t2=(34,66,8,90,61,44,22,67,974)
l1=list(t1)
l2=list(t2)
l1.extend(l2)
t1=tuple(l1)
print(t1)
