tasks = []

for i in range(3):
    task = input("Enter a task: ")
    tasks.append(task)

print("\nYour Tasks:")

for task in tasks:
    print("-", task)







weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height * height)

print("BMI =", bmi)