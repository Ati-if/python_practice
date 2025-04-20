def show_balance():
    print(f"Your balance is: ${balance}")


def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"${amount} deposited.")
    else:
        print("Deposit amount must be positive.")


def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount > 0 and amount <= balance:
        balance -= amount
        print(f"${amount} withdrawn.")
    elif amount > balance:
        print("Insufficient funds.")
    else:
        print("Withdrawal amount must be positive.")


balance = 0
is_running = True

while is_running:
    print("\nBanking Program")
    print("1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        is_running = False
        print("Exiting the program.")
    else:
        print("That is not a valid choice.")

print("Thank You! Have a nice day")