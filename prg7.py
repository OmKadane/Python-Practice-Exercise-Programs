total_bugs = 0

for day in range(1, 8):
    while True:
        try:
            bugs = int(input(f"Enter the number of bugs collected on day {day}: "))
            if bugs < 0:
                print("Please enter a non-negative number.")
                continue
            total_bugs += bugs
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

print("The total number of bugs collected over the seven days is:", total_bugs)