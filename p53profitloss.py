"""
Write a program where a user enters the buying price and selling price,
then the output should show if the person has made a profit or loss.
"""

buying_price=int(input("enter buying price:"))
selling_price=int(input("enter selling price:"))

if buying_price>selling_price:
    print("user has made a loss")
else:
    print("user has made a profit")