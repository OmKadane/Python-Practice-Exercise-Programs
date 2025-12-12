try:
    user_input = input("Please enter an integer: ")
    user_integer = int(user_input)
    print(f"You entered the integer: {user_integer}")
except ValueError:
    print("Invalid input. Please enter a whole number.")
finally:
    print("Input attempt finished.")
