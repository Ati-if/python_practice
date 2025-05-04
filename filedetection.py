import os

file_path = "excption.py"

if os.path.exists(file_path):
  print(f"{file_path} exists")
else:
  print(f"{file_path} does not exist")