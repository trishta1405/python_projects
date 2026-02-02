f1=open("abc","r")
f2=open("abc1","w")
data=f1.read()
for x in data:
    f2.write(x)

f1.close()
f2.close()
print("Copied")

"""
1) 1->2 copy space X
2) 1->2 copy vowel X
3) 1->2 vowel
    ->3 other
4) 1->2 upper
    ->3 lower


"""