# Python program that calculates the electricity bill based on the number of units used. As per the rates: Up to 100 units = ₹5 per unit, 101 to 300 units = ₹7 per unit and above 300 units = ₹10 per unit.
units = int(input("Enter the number of units used: "))

if units <= 100:
    print(f"Your electricity bill is: ₹{units * 5}")
elif 101 <= units <= 300:
    print(f"Your electricity bill is: ₹{units * 7}")
else:
    print(f"Your electricity bill is: ₹{units * 10}")
