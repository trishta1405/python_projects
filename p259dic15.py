"""
Create a Dictionary to store these monthly expenses and using that find out:
1. In February, how many dollars did you spend extra compared to January?
2. Calculate your total expenses for the first quarter (January to March) of the year.
3. Check if you spent exactly 2400 dollars in any month.
4. Modify the expense for June (2080 dollars) to your monthly expenses.
5. You returned an item that you bought in April and received a refund of 200 dollars.
6. Determine which month had the highest expense and print the month and the
amount.
7. Calculate the average monthly expense for the first half of the year (January to
June).
8. Find the month with the lowest expense and print the month and the amount.
"""

expenses={"January":2200,
"February":2350,
"March":2600,
"April":2130,
"May":2190,
"June":1980,
"July" :2400,
"August" :2250,
"September" :2100,
"October": 2400,
"November":2150,
"December":2500}

print("1. Extra spent in February:",
      expenses["February"] - expenses["January"])

first_quarter_total = expenses["January"] + expenses["February"] + expenses["March"]
print("2. First quarter total:", first_quarter_total)

print("3. Any month with expense 2400?",
      2400 in expenses.values())

expenses["June"] = 2080
print("4. Updated June expense:", expenses["June"])

expenses["April"] = expenses["April"] - 200
print("5. Updated April expense:", expenses["April"])

highest_month = max(expenses, key=expenses.get)
print("6. Highest expense:", highest_month, expenses[highest_month])

first_half_total = (
    expenses["January"] + expenses["February"] + expenses["March"] +
    expenses["April"] + expenses["May"] + expenses["June"]
)
average_first_half = first_half_total / 6
print("7. Average expense:", average_first_half)

lowest_month = min(expenses, key=expenses.get)
print("8. Lowest expense:", lowest_month, expenses[lowest_month])
