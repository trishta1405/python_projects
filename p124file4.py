f1=open("abc","r")
data=f1.read()
for x in data:
    if x=="a" or x=="A":
        pass
    else:
        print(x,end="")

f1.close()

"""
1) vowels?
2)space ?
3) upper ? lower ?
4) vowels X
5) space X
6) Vowel 7
"""