# Simple ATM in Python

# Initial account balance
balance = 1000.0

# Function to display menu
def show_menu():
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

# ATM
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print(f"\nYour current balance is: {balance:.2f}")

    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"{amount:.2f} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= balance:
            balance -= amount
            print(f"{amount:.2f} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please select between 1 and 4.")
