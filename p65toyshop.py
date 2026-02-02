"""
 A toy vendor supplies three types of toys: Battery-Based Toys, Key-Based
Toys, and Electrical Charging Based Toys.
The vendor gives a discount of 10% on orders for battery-based toys if the order is for
more than Rs. 1000. On orders of more than Rs. 100 for key-based toys, a discount of
5% is given, and a discount of 10% is given on orders for electrical charging-based toys
of value more than Rs. 500. Assume that the numeric codes 1, 2, and 3 are used for
battery-based toys, key-based toys, and electrical charging-based toys, respectively.
Write a program that reads the product code and the order amount and prints out the
net amount that the customer is required to pay after the discount.
"""
print("10% discount on battery based toys worth more than 1000")
print("10% discount on electrical charging based toys worth more than 1000")
print("10% discount on key based toys worth more than 1000")

print("1. Battery Based Toys")
print("2. Electrical Charging Based Toys ")
print("3. Key-Based Toys")

choice=int(input("enter your choice to see if you are eligible for discount:"))
if choice==1:
    print("a. car=1500")
    print("b. helicopter=3000")
    print("c. talking stuffed toy=600")
    BBT=input("enter your choice:")
    if BBT=="a":
        discount = (10 / 100) * 1500
        print("your discount for car worth 1500 will be", discount)
    elif BBT=="b":
        discount = (10 / 100) * 3000
    elif BBT=="c":
        print("there will be no discount")
    else:
        print("please enter valid choice")
elif choice==2:
    print("a. keyboard=500")
    print("b. lights=400")
    print("c. chargable car=900")
    a=500
    b=400
    c=900
    kbt=input("enter your choice to see if you are eligible for discount:")
    if kbt=="a":
        discount2 = (10 / 100) * 500
        print("your discount for keyboard will be", discount2)
    elif kbt=="b":
        print("you are not eligible for discount")
    elif kbt=="c":
        discount2 = (10 / 100) * 900
        print("your discount for chargable car will be", discount2)
    else:
        print("please enter valid choice")
elif choice==3:
    print("a. monkey=100")
    print("b. bear=70")
    print("c. doll=200")
    a=100
    b=70
    c=100
    cbt=input("enter your choice to see if you are eligible for discount:")
    if cbt=="a":
        Discount3 = (5 / 100) * 100
        print("your discount for keyboard will be", Discount3)
    elif cbt=="b":
        print("you are not eligible for discount")
    elif cbt=="c":
        Discount3 = (5 / 100) * 100
        print("your discount for doll will be", Discount3)
    else:
        print("please enter valid choice")
else:
    print("please enter valid choice")

