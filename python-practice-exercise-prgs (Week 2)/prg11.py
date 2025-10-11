# Code Review Checklist: Assume you have two files: required_checks.txt (mandatory checks) and performed_checks.txt (checks completed). Write a program that uses sets to determine and print which required checks were missed.
with open('python-practice-exercise-prgs (Week 2)/required_checks.txt', 'r') as required_file:
    required_checks = {line.strip() for line in required_file.readlines()}

with open('python-practice-exercise-prgs (Week 2)/performed_checks.txt', 'r') as performed_file:
    performed_checks = {line.strip() for line in performed_file.readlines()}

missed_checks = required_checks - performed_checks
print("Missed checks are:")
for check in missed_checks:
    print(check)
