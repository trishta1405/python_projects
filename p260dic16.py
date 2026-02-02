"""

info
[600,630,620]
ril
mtl
[1430,1490,1567]
[234,180,160]
Write a program that asks user for operation. Value of operations could be,
option 1, print: When user enters print it should print following,
info ==> [600, 630, 620] ==> avg:  616.67
ril ==> [1430, 1490, 1567] ==> avg:  1495.67
mtl ==> [234, 180, 160] ==> avg:  191.33
option 2, add: When user enters 'add', it asks for stock ticker and price. If stock already
exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will
create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==>
[560] to the dictionary of stocks.
"""

stocks = {
    "info": [600, 630, 620],
    "ril": [1430, 1490, 1567],
    "mtl": [234, 180, 160]
}

choice=input("enter operation (print / add): ")

if choice=="print":
    for k, v in stocks.items():
        avg_price = sum(v) / len(v)
        print(k, "==>",v, "==> avg:", round(avg_price, 2))

elif choice =="add":
    stock_name = input("enter stock name: ")
    price = int(input("enter stock price: "))

    if stock_name in stocks:
        stocks[stock_name].append(price)
    else:
        stocks[stock_name] = [price]

    print("updated stocks:")
    print(stocks)

else:
    print("invalid operation")
