ch=input("enter any character")
a=ord(ch)

if a>=97 and a<=122:
    print(chr(a-32))
elif a>=65 and a<=90:
    print(chr(a+32))
else:
    print("Other")