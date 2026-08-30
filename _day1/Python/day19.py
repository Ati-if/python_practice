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






number = int(input("Enter a number: "))

for i in range(1, number + 1):
    if number % i == 0:
        print(i)






number = int(input("Enter a number: "))

count = 0

for i in range(1, number + 1):
    if number % i == 0:
        count += 1

print("Number of factors =", count)