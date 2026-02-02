ch=input("enter any character")
a=ord(ch)#converts character into ascii value
#checking weather a character is uppercase or lowercase using ascii
if a>=97 and a<=122:
    print( ch ,"in lower case")
elif a>=65 and a<=90:
    print(f" {ch} in upper case")
else:
    print("Other")