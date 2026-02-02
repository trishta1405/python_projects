f1=open("abc","r")
data=f1.read()
c=0
d=0
e=0
for x in data:
        if x.isupper():
            d=d+1
        elif x.islower():
            e=e+1
        else:
            c=c+1

f1.close()
print("Total uppercase letters are= ",d)
print("Total lowercase letters are= ",e)
print("Total other letters are= ",c)