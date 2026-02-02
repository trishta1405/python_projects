f1=open("abc","r")
f2=open("abc5","w")
data=f1.read()
for x in data:
    f2.write(x.swapcase())

f1.close()
f2.close()
print("Copied")

