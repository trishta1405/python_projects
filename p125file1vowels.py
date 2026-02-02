f1=open("abc","r")
data=f1.read()
c=0
for x in data:
    if x=="a" or x=="A" or x=="e" or x=="E" or x=="i" or x=="I" or x=="u"or x=="U" or x=="u"or x=="U":
        c=c+1

f1.close()
print("Total vowels are= ",c)