"""
 Write a Python program to input any alphabet and check whether it is a
vowel or consonant.
"""
alphabet=["a","e","i","o","u"]
char=input("please enter the character:")
if char in alphabet:
    print("char is a vowel")
else:
    if len(char)==1:
        print("char is a other")
    else:
        print("It is not a single character")