f1=open("abc","r")
data=f1.read()

for x in data:
        if x.isupper():
            print(x.lower(),end="")
        elif x.islower():
            print(x.upper(),end="")
        else:
            print(x,end="")

f1.close()