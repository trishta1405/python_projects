# Write a Python program to count the occurrences of an item in a tuple.

c=0
t1=(11,34,56,4,33,667,32,89,11,11,11)
num=int(input("Enter a number from the tuple:"))
for x in t1:
    if x==num:
        c=c+1
print(c)
