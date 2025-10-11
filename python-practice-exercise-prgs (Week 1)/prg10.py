num_of_students = int(input("Enter the number of students: "))
num_of_subjects = int(input("Enter the number of subjects per student: "))

for student in range(1, num_of_students + 1):
    total_score = 0.0
    for subject in range(1, num_of_subjects + 1):
        while True:
            try:
                score = float(input(f"Enter the score for subject {subject} of student {student}: "))
                if score < 0:
                    print("Please enter a non-negative score.")
                    continue
                total_score += score
                break
            except ValueError:
                print("Invalid input. Please enter a valid score.")
                continue
    average_score = total_score / num_of_subjects
    print(f"Total score for student {student} is: {total_score}")
    print(f"Average score for student {student} is: {average_score:.2f}")
    