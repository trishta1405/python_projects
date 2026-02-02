f1=open("abc","r")
f2=open("abc1","w")
data=f1.read()
for x in data:
    if x==" ":
        pass
    else:
        f2.write(x)

f1.close()
f2.close()
print("Copied")




