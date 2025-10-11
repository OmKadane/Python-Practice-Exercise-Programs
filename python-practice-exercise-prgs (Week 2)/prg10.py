raw_data = [105, 112, 98, 120]
normalized_data = [value / 100.0 for value in raw_data]

with open('python-practice-exercise-prgs (Week 2)/normalized.txt', 'w') as file:
    for value in normalized_data:
        file.write(f"{value}\n")
