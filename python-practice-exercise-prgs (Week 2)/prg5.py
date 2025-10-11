# Power Calculation: Write a function calculate_power(base, exponent) that takes two required numerical arguments and returns the result. Call the function and use an f-string to print the result, rounded to one decimal place.
def calculate_power(base, exponent):
    return base ** exponent

result = calculate_power(5, 3)
print(f"The result rounded to one decimal place is: {result:.1f}")
