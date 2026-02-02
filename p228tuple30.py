"""create a list of your friends' names and now create a list of tuples. The tuple should
contain the friend’s name and the length of the name. For Example: if someone’s name
is Aditya, the tuple would be: (‘Aditya’, 6) """


l1=["amit","misti","siddhu","riya","aanshi","bhumi"]
l2=[]
for x in l1:
    l2.append((x,len(x)))

t1=tuple(l2)
print(t1)

