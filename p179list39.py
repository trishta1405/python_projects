india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("Enter a city name: ")

if city in india:
    print("India")
elif city in pakistan:
    print("Pakistan")
elif city in bangladesh:
    print("Bangladesh")
else:
    print("City not found")
