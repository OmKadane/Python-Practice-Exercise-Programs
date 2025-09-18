budget = float(input("Enter your budget for the month: "))
total_expenses = 0.0

while True:
    try:
        expense = float(input("Enter an expense (or a negative number to finish): "))
        if expense < 0:  # If the user enters a negative number, the loop will end
            break
        total_expenses += expense
    except ValueError:
        print("Invalid input. Please enter a valid expense amount.")

if total_expenses > budget:
    print("You are over budget by:", total_expenses - budget)
else:
    print("You are under budget by:", budget - total_expenses)
    