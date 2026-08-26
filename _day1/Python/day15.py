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





secret = 25

for attempt in range(5):
    guess = int(input("Guess the number: "))

    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too small")
    else:
        print("Too large")
else:
    print("You lost! The number was", secret)