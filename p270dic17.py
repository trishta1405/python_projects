"""
 You and your wife argued about expenses last night. You both want to know who is
spending more in a month. Now you both go to the Little Yoda he is a good python
programmer. He suggested that both of you add an entry in a dictionary next time you
spend money. So that you can have a clear picture of your expenses and plan to reduce
them. Both dictionaries are as below-

Find out the total expenses for each of you.
Find out who spending more
Find out which thing you and your wife spending more
"""

ur_expenses={
"Clothes":1100,
"Shoes":1000,
"Watch":900,
"Mobile Recharge":699,
"Petrol":1980}

Wife_expenses={
"Mobile Recharge": 799,
"DTH recharge":999,
"Clothes":2310,
"Makeup":3670,
"Shoes":999}

total_expenses= ur_expenses["Clothes"] + ur_expenses["Shoes"] + ur_expenses["Watch"]+ ur_expenses["Mobile Recharge"] + ur_expenses["Petrol"]
print("total expense of husband is:",total_expenses)

total_expenses2=Wife_expenses["Mobile Recharge"]+Wife_expenses["DTH recharge"]+Wife_expenses["Clothes"]+Wife_expenses["Shoes"]+Wife_expenses["Makeup"]
print("total expense of wife is:",total_expenses2)
print(" ")
if total_expenses2>total_expenses:
    print("Total expense of wife is more than husband's expense")
else:
    print("Total expense of wife is not more than husband's expense")
print(" ")
print("Husband spend most on:",max(ur_expenses.keys()))
print("wife spend most on:",max(Wife_expenses.keys()))
