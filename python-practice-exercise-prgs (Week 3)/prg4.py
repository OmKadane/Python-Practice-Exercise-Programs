import random

def roll_dice(sides):
    return random.randint(1, sides) # Or return random.choice(range(1, sides))

# Test the function
result = roll_dice(6)
print(f"You rolled a {result} on a 6-sided die.")
