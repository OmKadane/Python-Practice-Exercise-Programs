sum = 0.0

while True:
    try:
        num = float(input("Enter a series of positive numbers or a negative number to finish: "))
        if num < 0: # If the user enter a negative number, the loop will end
            break
        sum += num
    except ValueError:
        print("Invalid input. Please enter a valid positive number.")
print("The sum of the positive numbers is:", sum)