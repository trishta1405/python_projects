
while True:
    print("press 1 for square")
    print("press 2 for cube")
    print("press 3 to exit")
    op=int(input("enter your option"))
    if op==1:
        num1=int(input("enter a number"))
        square = num1 * num1
        print(f"square of {num1} is {square}")
    elif op==2:
        num2=int(input("enter a number"))
        square = num2 * num2 * num2
        print(f"square of {num2} is {square}")
    elif op==3:
        print("Bye")
        break
    else:
        print("enter option")