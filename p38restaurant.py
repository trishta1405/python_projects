print("press 1 for pizza")
print("press 2 for burger")
print("press 3 for momos")
print("press 4 for sandwich")
og=int(input("enter your choice:"))
if og==1:
    a= 200
    b=300
    c=450
    d=520
    print("1. onion pizza=200")
    print("2. pepper pizza=300")
    print("3. farm pizza=450")
    print("4. margerita pizza=520")

    pizza=int(input("please enter your choice:"))
    if pizza==1:
         quantity_of_product= int(input("please enter number the quantity:"))
         print("bill=",quantity_of_product*a)
    elif pizza==2:
        quantity_of_product= int(input("please enter number the quantity:"))
        print("bill=", quantity_of_product*b)
    elif pizza==3:
         quantity_of_product= int(input("please enter number the quantity:"))
         print("bill=", quantity_of_product*c)
    elif pizza==4:
         quantity_of_product= int(input("please enter number the quantity:"))
         print("your bill is=", quantity_of_product*d)
    else:
        print("please enter a valid choice")



elif og==2:
    print("1. veggie burger=100")
    print("2. aloo sandwich=120")
    print("3. aloo grill sandwich=140")
    print("4. aloo veggie sandwich=150")
    print("5. veggie sandwich=180")
    print("6. loaded sandwich=200")
    a = 100
    b = 120
    c = 140
    d = 150
    e = 180
    f = 200
    burger= int(input("please enter your choice:"))
    if burger == 1:
        quantity_of_product = int(input("please enter number the quantity:"))
        print("bill=", quantity_of_product * a)
    elif burger == 2:
        quantity_of_product = int(input("please enter number the quantity:"))
        print("bill=", quantity_of_product * b)
    elif burger== 3:
        quantity_of_product = int(input("please enter number the quantity:"))
        print("bill=", quantity_of_product * c)
    elif burger == 4:
        quantity_of_product = int(input("please enter number the quantity:"))
        print("bill=", quantity_of_product * d)
    elif burger == 5:
        quantity_of_product = int(input("please enter number the quantity:"))
        print("bill=", quantity_of_product * e)
    elif burger == 6:
        quantity_of_product = int(input("please enter number the quantity:"))
        print("your bill is=", quantity_of_product * f)

    else:
        print("please enter a valid choice")


elif og==3:
    a=80
    b=90
    c=100
    d=110
    print("1. veg momos=80")
    print("2. paneer momos=90")
    print("3. veg fried momos=100")
    print("4. paneer fried momos=110")
    momos = int(input("please enter your choice:"))
    if momos == 1:
        quantity_of_product = int(input("please enter number the quantity:"))
        print("bill=", quantity_of_product * a)
    elif momos == 2:
        quantity_of_product = int(input("please enter number the quantity:"))
        print("bill=", quantity_of_product * b)
    elif momos == 3:
        quantity_of_product = int(input("please enter number the quantity:"))
        print("bill=", quantity_of_product * c)
    elif momos == 4:
        quantity_of_product = int(input("please enter number the quantity:"))
        print("your bill is=", quantity_of_product * d)
    else:
        print("please enter a valid choice")

elif og==4:
    a=100
    b=130
    c=150
    d=180
    print("1. veg sandwich=100")
    print("2. aoo sandwich=130")
    print("3. aloo cheese sandwich=150")
    print("4. aloo veg sandwich=180")
    sandwich = int(input("please enter your choice:"))
    if sandwich == 1:
        quantity_of_product = int(input("please enter number the quantity:"))
        print("bill=", quantity_of_product * a)
    elif sandwich == 2:
        quantity_of_product = int(input("please enter number the quantity:"))
        print("bill=", quantity_of_product * b)
    elif sandwich == 3:
        quantity_of_product = int(input("please enter number the quantity:"))
        print("bill=", quantity_of_product * c)
    elif sandwich == 4:
        quantity_of_product = int(input("please enter number the quantity:"))
        print("your bill is=", quantity_of_product * d)
    else:
        print("please enter a valid choice")
else:
    print("please enter a valid choice")






