days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

try:
    num = int(input("Enter a number (1-7): "))
    days_index = num % 7
    print(f"The day is: {days[days_index]}.")
except ValueError:
    print("Invalid input! Please enter a valid number (1-7).")