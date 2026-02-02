f1=open("abc","r")
f2=open("abc2","w")
data=f1.read()
for x in data:
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u" or x=="A" or x=="E" or x=="I" or x=="O" or x=="U":
        pass
    else:
        f2.write(x)

f1.close()
f2.close()
print("Copied")