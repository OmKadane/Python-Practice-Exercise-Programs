temperatures = [78.5, 99.2, 101.5, 85.0, 98.6, 102.1]

high_temperatures = [temp for temp in temperatures if temp > 100.0]
print(f"Temperatures above 100.0°F are: {high_temperatures}")