units = int(input("Enter the number of units used: "))

if units <= 100:
    print(f"Your electricity bill is: ₹{units * 5}")
elif 101 <= units <= 300:
    print(f"Your electricity bill is: ₹{units * 7}")
else:
    print(f"Your electricity bill is: ₹{units * 10}")