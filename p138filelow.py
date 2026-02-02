f1=open("abc","r")
f2=open("abc6","w")
f3=open("abc7","w")
data=f1.read()
for x in data:
    if x.isupper():
        f2.write(x)
    else:
        f3.write(X)

f1.close()
f2.close()
print("Copied")