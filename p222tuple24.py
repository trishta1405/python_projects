#Write a Python program to unpack a tuple into several variables.

t1=(23,45,88,54,34,46,89,22,67,99)
t2=("a=","b=","c=","d=","e=","f=","g=","h=","i=","j=")
for x in t1:
    for y in t2:
        print(y,x)