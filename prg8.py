calories_per_minute = 3.9

for minutes in range(10, 31, 5):
    calories_burned = calories_per_minute * minutes
    print(f"Calories burned after {minutes} minutes: {calories_burned:.2f}")