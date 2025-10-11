with open('python-practice-exercise-prgs (Week 2)/readings.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file.readlines()]
print(numbers)