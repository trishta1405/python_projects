f1=open("abc","r")
f2=open("abc7","w")
data=f1.read()
for x in data:
    if x.islower():
        f2.write(x)
    else:
        pass

f1.close()
f2.close()
print("Copied")