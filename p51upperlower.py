
char=input("enter character:")
if char.isupper():   #checks if character is upper
    print(char.lower())   #converts the charater from upper to lower
elif char.islower():    #checks if the character is lower
    print(char.upper())     #converts the character is lower to upper
else:
    print(char)