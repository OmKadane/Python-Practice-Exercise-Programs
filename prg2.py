# Program to ask a user for their age and decides whether they are allowed to vote (age 18 and up) or not. And if not, to display how many years are left until they can vote.
age = int(input("Please enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    years_left = 18 - age
    print(f"You are not eligible to vote. You have to wait {years_left} more years.")
