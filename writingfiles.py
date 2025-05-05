import json
import csv

employees = [["name", "age" , "job"],
             ["Spongebob", 30 , "Cook"],
             ["Alex", 40 , "Writer"],
             ["Mark", 50 , "Manager"]]


file_path = "C:/Users/DELL/Desktop/output.json"
file_path = "C:/Users/DELL/Desktop/output.csv"

try:
   with open(file_path, "w") as file:
    json.dump(employees, file, indent=5)
    print(f"json file '{file_path}' was created")
except Exception as e:
  print(f" {file_path}: {e}")