"""
 Write a program to see if the entered letter is in upper case or lower case.
"""
"""
char=input("enter character:")
character=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","v","w","x","y","z"]
num=["1","2","3","4","5","6","7","8","9","0"]
if char in character:
    print("char is in lower case")
elif char in num:
    print("char is an integer")
else:
    print("char is in upper case")
"""
char=input("enter character:")
if char.isupper():
    print("char is in upper case")
elif char.islower():
    print("char is in lower case")
else:
    print("Other character  ")