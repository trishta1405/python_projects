"""
. Ask the user to enter age, gender (M or F), marital status (Y or N), and then
using the following rules, print their place of service:
• If the employee is female, she will work only in urban areas.
• If the employee is male and age is between 20 to 40, he may work anywhere.
• If the employee is male and age is between 40 to 60, he will work in urban areas
only.
• Any other input of age should print "ERROR".
"""

age = int(input("please enter your age: "))
gender = input("please enter your gender (M or F): ")
marital_status = input("please enter your marital status (married or not): ")

if gender=="f" or "F":
    print("you are working in urban areas")
elif gender=="m" or "M" and 40>=age>=20:
    print("you can work in any areas")
elif gender=="m" or "M" and 60>=age>=40:
    print("you are working in urban areas")
else:
    print("error")
