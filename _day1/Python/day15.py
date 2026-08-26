print("1. Say Hello")
print("2. Say Goodbye")
print("3. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Hello!")
elif choice == 2:
    print("Goodbye!")
elif choice == 3:
    print("Program ended")
else:
    print("Invalid choice")