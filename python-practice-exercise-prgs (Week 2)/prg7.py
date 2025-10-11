def calculate_mean(*numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
mean_of_three_numbers = calculate_mean(10, 20.88, 30)
mean_of_five_numbers = calculate_mean(5, 10.5, 15, 20.75, 25)

print(f"Mean of three numbers: {mean_of_three_numbers}")
print(f"Mean of five numbers: {mean_of_five_numbers}")