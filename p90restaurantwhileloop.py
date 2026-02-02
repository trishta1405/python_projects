total_bill = 0
while True:
    print("press 1 for pizza")
    print("press 2 for burger")
    print("press 3 for momos")
    print("press 4 for sandwich")
    print("press 5 for exit")
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
             bill_1 = quantity_of_product * a
             print("bill=",bill_1)
             total_bill= total_bill+bill_1
        elif pizza==2:
            quantity_of_product= int(input("please enter number the quantity:"))
            bill_2 = quantity_of_product * b
            print("bill=", bill_2)
            total_bill= total_bill+bill_2
        elif pizza==3:
             quantity_of_product= int(input("please enter number the quantity:"))
             bill_3 = quantity_of_product * c
             print("bill=", bill_3)
             total_bill= total_bill+bill_3
        elif pizza==4:
             quantity_of_product= int(input("please enter number the quantity:"))
             bill_4 = quantity_of_product * d
             print("your bill is=", bill_4)
             total_bill= total_bill+bill_4

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
            bill_a = quantity_of_product * a
            print("bill=", bill_a)
            total_bill = total_bill + bill_a
        elif burger == 2:
            quantity_of_product = int(input("please enter number the quantity:"))
            bill_b = quantity_of_product * b
            print("bill=", bill_b)
            total_bill = total_bill + bill_b
        elif burger== 3:
            quantity_of_product = int(input("please enter number the quantity:"))
            bill_c = quantity_of_product * c
            print("bill=", bill_c)
            total_bill = total_bill + bill_c
        elif burger == 4:
            quantity_of_product = int(input("please enter number the quantity:"))
            bill_d = quantity_of_product * d
            print("bill=", bill_d)
            total_bill = total_bill + bill_d
        elif burger == 5:
            quantity_of_product = int(input("please enter number the quantity:"))
            bill_e=quantity_of_product * e
            print("bill=", bill_e)
            total_bill = total_bill + bill_e
        elif burger == 6:
            quantity_of_product = int(input("please enter number the quantity:"))
            bill_f=quantity_of_product * f
            print("your bill is=", bill_f)
            total_bill = total_bill + bill_f

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
            billa = quantity_of_product * a
            print("bill=",billa)
            total_bill = total_bill + billa
        elif momos == 2:
            quantity_of_product = int(input("please enter number the quantity:"))
            billb = quantity_of_product * b
            print("bill=", billb)
            total_bill = total_bill + billb
        elif momos == 3:
            quantity_of_product = int(input("please enter number the quantity:"))
            billc = quantity_of_product * c
            print("bill=", billc)
            total_bill = total_bill + billc
        elif momos == 4:
            quantity_of_product = int(input("please enter number the quantity:"))
            billd = quantity_of_product * d
            print("your bill is=", billd)
            total_bill = total_bill + billd
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
            bill1 = quantity_of_product * a
            print("bill=",bill1)
            total_bill = total_bill + bill1
        elif sandwich == 2:
            quantity_of_product = int(input("please enter number the quantity:"))
            bill2 = quantity_of_product * b
            print("bill=",bill2)
            total_bill = total_bill + bill2
        elif sandwich == 3:
            quantity_of_product = int(input("please enter number the quantity:"))
            bill3 = quantity_of_product * c
            print("bill=",bill3)
            total_bill = total_bill + bill3
        elif sandwich == 4:
            quantity_of_product = int(input("please enter number the quantity:"))
            bill4 = quantity_of_product * d
            print("bill=",bill4)
            total_bill = total_bill + bill4
        else:
            print("please enter a valid choice")
    elif og==5:

        print(f"your total bill is {total_bill}")
        print("thank you!")
        break

    else:
        print("please enter a valid choice")

