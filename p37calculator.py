print("press 1 for addition:")
print("press 2 for subtraction:")
print("press 3 for multiplication:")
print("press 4 for division:")
print("press 5 for exponentiation:")
op=int(input("enter your choice:"))
if op==1:
    number1 = int(input("enter number1:"))
    number2 = int(input("enter number2:"))
    print("addition of 2 numbers are:", number1+number2)
elif op==2:
    number1 = int(input("enter number1:"))
    number2 = int(input("enter number2:"))
    print("subtraction of 2 numbers are:", number1-number2)
elif op==3:
    number1 = int(input("enter number1:"))
    number2 = int(input("enter number2:"))
    print("multiplication of 2 numbers are:", number1*number2)
elif op==4:
    number1 = int(input("enter number1:"))
    number2 = int(input("enter number2:"))
    print("division of 2 numbers are:", number1/number2)
elif op==5:
    number1 = int(input("enter number1:"))
    number2 = int(input("enter number2:"))
    print("exponentiation of 2 numbers are:", number2**number2)
else:
    print("please enter a valid choice")

"""
cont=int(input("press 1 to continue:"))
  if cont==1:
    op=int(input("enter your choice:"))
        if op == 1:
          print("addition of 2 numbers are:", number1 + number2)
        elif op == 2:
          print("subtraction of 2 numbers are:", number1 - number2)
        elif op == 3:
          print("multiplication of 2 numbers are:", number1 * number2)
        elif op == 4:
          print("division of 2 numbers are:", number1 / number2)
        elif op == 5:
          print("exponentiation of 2 numbers are:", number2 ** number2)
        else:
          print("please enter a valid choice")

  else:
print("thank you")
"""