"""
Create a Python program that checks if a person's BMI (Body Mass Index)
is underweight, normal weight, overweight, or obese. Use the following
categories: underweight (BMI < 18.5), normal (18.5 ≤ BMI < 24.9), overweight (25 ≤
BMI < 29.9), and obese (BMI ≥ 30). Ask the user to enter their BMI and print the
corresponding category.
"""

weight=float(input("enter your weight in kgs: "))
height = float(input("enter your height in m: "))

bmi=weight/(height*height)

if bmi<18.5:
    print("you are underweight and your bmi is",bmi)
elif 18.5<= bmi<24.9:
    print("you are normal and your bmi is",bmi)
elif 25 <= bmi<29.9:
    print("you are overweight and your bmi is",bmi)
else:
    print("you are obese and your bmi is",bmi)
