"""
A company decided to give a bonus of 5% to employees if their year of
service is more than 5 years.
"""


year = int(input("please enter the number of years you are working in this company: "))
if year>=5:
    salary = int(input("enter your salary:"))
    print("your bonus will be:", 5/100*salary)
else:
    print("you are not eligible for the bonus")
