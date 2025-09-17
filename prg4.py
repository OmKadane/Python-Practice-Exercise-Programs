# Program to prompt the user to enter the temperature in Celsius and classifies it as: Below 0°C → Freezing, 0°C to 20°C → Cold, 21°C to 30°C → Warm, Over 30°C → Hot

celsius = float(input("Enter the temperature in Celsius: "))

if celsius < 0:
    print("Freezing")
elif 0 <= celsius <= 20:
    print("Cold")
elif 21 <= celsius <= 30:
    print("Warm")
else:
    print("Hot")
