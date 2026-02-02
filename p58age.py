#Write a program to check whether a person is a senior citizen or not.

age=int(input("Enter the age:"))

if age>=18 and age<=59:
    print("he is an adult")
elif age>=60:
    print("he is a senior citizen")
elif age<=18 and age>=0:
    print("he is a children")
else:
    print("please enter valid age")