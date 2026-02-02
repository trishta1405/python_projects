"""
. You bought 9 packets of potato chips from a store. Each packet costs 1.49
dollar and you gave shopkeeper 20 dollar. Find out using python, how
many dollars is the shopkeeper going to give you back?
"""

quantity=int(input("please enter the quantity:"))
bill=quantity*1.49
money_given=int(input("please enter the amount you gave to shopkeeper:"))
print("money shopkeeper gave=",money_given-bill)
