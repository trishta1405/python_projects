print("Press 1 for Square")
print("Press 2 for Cube")
op=int(input("enter your choice:"))

if op==1:
    number=int(input("enter first number:"))
    print("square of number",number*number)
elif op==2:
    number = int(input("enter first number:"))
    print("cube of number",number*number*number)
else:
    print("wrong choice")