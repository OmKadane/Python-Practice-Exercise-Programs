a = float(int(input("Enter 1st number: ")))
b = float(int(input("Enter 2nd number: ")))
c = float(int(input("Enter 3rd number: ")))

if (a > b) and (a > c):
    print(f"{a} is the largest number")
elif (b > a) and (b > c):
    print(f"{b} is the largest number")
elif (c > a) and (c > b):
    print(f"{c} is the largest number")
else:
    print("All are equal")