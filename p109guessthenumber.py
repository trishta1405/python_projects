import random
x=random.randint(1,50)
c=0
y=0
st=1
ending=50
while x!=y:
    print(f"your new range is {st}-{ending}")
    y=int(input("enter the number : "))
    c=c+1
    if x==y:
        print(f"correct number is {y}")
    elif x<y:
        print(f"please think less than {y}")
        ending=y
    else:
        print(f"please think greater than {y}")
        st=y
print("number of tries are:", c)
