stock_levels = [150, 45, 210, 8, 90, 300, 12]
middle_three_items = stock_levels[2:5]

stock_levels.insert(0, 180)
print(f"Middle three items are: {middle_three_items}")
print(f"Updated stock levels: {stock_levels}")
