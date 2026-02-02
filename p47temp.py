"""
Write a program where the user enters the temperature and display a
message according to the temperature:
Temp < 0: Freezing Atmosphere
• Temp 0 to 10: Very cold atmosphere
• Temp 10 to 20: Cold Atmosphere
• Temp 20 to 30: Normal Atmosphere
• Temp 30 to 40: Hot atmosphere
• Temp > 40: Very hot atmosphere
"""

temperature = int(input("Enter the temperature: "))
if temperature < 0:
    print("it is a Freezing Atmosphere ")
elif temperature > 0 and temperature < 10:
    print("it is a very cold Atmosphere ")
elif temperature > 10 and temperature < 20:
    print("it is a cold Atmosphere ")
elif temperature > 20 and temperature < 30:
    print("it is a Normal Atmosphere ")
elif temperature > 30 and temperature < 40:
    print("it is a Hot Atmosphere ")
else:
    print("it is a Very Hot Atmosphere ")