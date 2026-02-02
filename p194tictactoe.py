list1 = ["A1", "A2", "A3"]
list2 = ["B1", "B2", "B3"]
list3 = ["C1", "C2", "C3"]

print(list1)
print(list2)
print(list3)

list11=["_", "_", "_"]
list22=["_", "_", "_"]
list33=["_", "_", "_"]

print(list11)
print(list22)
print(list33)

turn = 1
while turn < 10:
    print("After turn", turn)
    a = input("enter your choice: ")

    turn=turn+1
    if a == "A1":
            choice1 = input("enter your choice (x or o): ")
            list11[0] = choice1
            print(list11)
            print(list22)
            print(list33)

    elif a == "A2":
            choice1 = input("enter your choice (x or o): ")
            list11[1] = choice1
            print(list11)
            print(list22)
            print(list33)

    elif a == "A3":
            choice1 = input("enter your choice (x or o): ")
            list11[2] = choice1
            print(list11)
            print(list22)
            print(list33)
    elif a == "B1":
            choice1 = input("enter your choice (x or o): ")
            list22[0] = choice1
            print(list11)
            print(list22)
            print(list33)
    elif a == "B2":
            choice1 = input("enter your choice (x or o): ")
            list22[1] = choice1
            print(list11)
            print(list22)
            print(list33)
    elif a == "B3":
            choice1 = input("enter your choice (x or o): ")
            list22[2] = choice1
            print(list11)
            print(list22)
            print(list33)
    elif a == "C1":
            choice1 = input("enter your choice (x or o): ")
            list33[0] = choice1
            print(list11)
            print(list22)
            print(list33)
    elif a == "C2":
            choice1 = input("enter your choice (x or o): ")
            list33[1] = choice1
            print(list11)
            print(list22)
            print(list33)
    elif a == "C3":
            choice1 = input("enter your choice (x or o): ")
            list33[2] = choice1
            print(list11)
            print(list22)
            print(list33)

    else:
        print("not true")

if








