celsius = float(input("Enter the temperature in Celsius: "))

if celsius < 0:
    print("Freezing")
elif 0 <= celsius <= 20:
    print("Cold")
elif 21 <= celsius <= 30:
    print("Warm")
else:
    print("Hot")
