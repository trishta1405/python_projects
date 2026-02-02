f1=open("abc","r")
data=f1.read()
c=0
for x in data:
    if x==" ":
        c=c+1

f1.close()
print("Total vowels are= ",c)