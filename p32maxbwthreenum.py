number1=int(input("enter number1:"))
number2=int(input("enter number2:"))
number3=int(input("enter number3:"))

if number1>number2 and number1>number3:
    print("number1 is greatest")
elif number2>number1 and number2>number3:
    print("number2 is greatest")
else:
    print("number3 is greatest")