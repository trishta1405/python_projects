#Write a Python program to remove an item from a tuple.


t1=(11,34,56,4,33,667,32,89)
l1=list(t1)
num=int(input("Enter a number to remove from the tuple:"))
l1.remove(num)
t1=tuple(l1)
print(t1)