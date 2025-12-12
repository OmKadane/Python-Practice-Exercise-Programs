class InvalidAgeError(Exception):
    pass
def check_age(age):
    if age < 0 or age > 110:
        raise InvalidAgeError("Age must be between 0 and 110.")
    else:
        print(f"Age {age} is valid.")

# Example usage:
try:
    age_input = int(input("Enter your age: "))
    check_age(age_input)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
