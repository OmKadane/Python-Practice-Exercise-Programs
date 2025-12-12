import csv

with open('students.csv', 'r') as file:
    csv_reader = csv.reader(file)
    
    next(csv_reader) # Used to skip the header row (id,name,city)
    
    print("----------------------------")
    print("      Students Records     ")
    print("----------------------------")
    for row in csv_reader:
        print(f"Student ID: {row[0]}")    
        print(f"Student Name: {row[1]}")  
        print(f"Student Roll No: {row[2]}")
        print(f"Student City: {row[3]}")  
        print("----------------------------")
