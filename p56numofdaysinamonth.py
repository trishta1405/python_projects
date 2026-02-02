#Write a Python program to find the number of days in a month.

month=int(input("Enter the month number:"))

if month==1:
    print("january has 31 days")
elif month==3:
    print("March has 31 days")
elif month==4:
    print("April has 30 days")
elif month==5:
    print("may has 31 days")
elif month==6:
    print("June has 30 days")
elif month==7:
    print("July has 31 days")
elif month==8:
    print("August has 31 days")
elif month==9:
    print("September has 30 days")
elif month==10:
    print("October has 31 days")
elif month==11:
    print("November has 30 days")
elif month==12:
    print("December has 31 days")
elif month==2:
    year=int(input("Enter the year:"))
    if year%4==0 and year%100!=0 or year%400==0:
        print("february has 29 days")
    else:
        print("february has 28 days")
else:
    print("Please enter a valid month")