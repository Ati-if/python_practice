tasks = []

for i in range(3):
    task = input("Enter a task: ")
    tasks.append(task)

print("\nYour Tasks:")

for task in tasks:
    print("-", task)