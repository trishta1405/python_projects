# Write a Python program to add an item in a tuple.

t1=(11,34,56,4,33,667,32,89)
l1=list(t1)
num=int(input("Enter a number to add in the tuple:"))
l1.append(num)
t1=tuple(l1)
print(t1)
