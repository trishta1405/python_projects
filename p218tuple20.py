#Write a Python program to find the index of an item in a tuple.

t1=(11,34,56,4,33,667,32,89)
num=int(input("Enter a number from the tuple:"))
if num in t1:
    print(t1.index(num))
else:
    print("num not in tuple")