f1=open("abc","r")
data=f1.read()
for x in data:
    if x==" ":
        pass
    else:
        print(x,end="")

f1.close()
