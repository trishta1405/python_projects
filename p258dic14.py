"""
Write a program that asks user for 4 type of inputs,
option 1 print: if user enter print then it should print all countries with their population in
this format,
china==>143
india==>136
usa==>32
uk==>21
option 2 add: if user input add then it should further ask for a country name to add.
If country already exist in our dataset then it should print that it exist and do nothing. If
it doesn't then it asks for population and add that new country/population in our dictionary
and print it
option 3 remove: when user inputs remove it should ask for a country to remove. If
country exist in our dictionary then remove it and print new dictionary using format shown
above in (a). Else print that country doesn't exist!
option 4 query: on this again ask user for which country he or she wants to query. When
user inputs that country it will print population of that country.
"""

while True:
    Country_Population={
    "China":143,
    "India":136,
    "USA":32,
    "UK":21
    }

    print("enter 'print' to print all the countries with their population")
    print("Enter 'add' to add a country")
    print("Enter 'remove' to remove a country")
    print("Enter 'query' to query a country or a population")
    print("Enter 'exit' to exit the program")
    enter=input("enter your choice:")

    if "print" in enter:
        print(Country_Population)
    elif "add" in enter:
        country_name=input("enter your country name:")
        population=input("enter your population:")
        Country_Population[country_name]=population
        print(Country_Population)
    elif "remove" in enter:
        country_name=input("enter your country name:")
        del Country_Population[country_name]
        print(Country_Population)
    elif "query" in enter:
        country_name=input("enter your country name:")
        if country_name in Country_Population:
            for k , v in Country_Population.items():
                if k==country_name:
                    print(k,v)
        else:
            print("country not exist")
    elif "exit" in enter:
        print("Thank you for using this program")
        break
    else:
        print("Please enter a valid input")
