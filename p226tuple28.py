#Write a Python program to sort a tuple of numbers in ascending order.

t1=(11,34,56,4,33,667,32,89,11,11,11)
l1=list(t1)
l1.sort()
t1=tuple(l1)
print(t1)