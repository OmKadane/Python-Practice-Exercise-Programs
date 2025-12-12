import os
from datetime import datetime

file_path = os.path.join(os.getcwd(), 'report.txt')
print(f"Full file path: {file_path}")

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%d/%m/%Y %H:%M:%S")
print(f"Current date and time: {formatted_datetime}")
