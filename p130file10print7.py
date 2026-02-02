f1=open("abc","r")
data=f1.read()

for x in data:
    if x=="a" or x=="A" or x=="e" or x=="E" or x=="i" or x=="I" or x=="o"or x=="O" or x=="u"or x=="U":
        print("7",end="")
    else:
        print(x,end="")
f1.close()