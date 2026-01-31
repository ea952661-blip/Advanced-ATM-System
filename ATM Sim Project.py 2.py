# Transactional ATM Simulation with Savings Account Feature

transactions = []
balance = 5000.0
savings_balance = 0.0
has_savings = False

print("Welcome to Bank of America ATM")

# Create PIN
while True:
    create_pin = input("Create a 4-digit PIN: ")
    if create_pin.isdigit() and len(create_pin) == 4:
        print("PIN created successfully.\n")
        break
    else:
        print("Invalid PIN. Try again.")

# Main ATM loop
while True:
    entered_pin = input("Enter your PIN: ")

    if entered_pin != create_pin:
        print("Incorrect PIN.\n")
        continue

    print("\n--- Main Menu ---")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Open savings account")
    print("5. More options (Savings)")
    print("6. View transaction history")
    print("7. Exit")

    choice = input("Select an option (1-7): ")

    if choice == "1":
        print(f"Balance: ${balance:.2f}")

    elif choice == "2":
        amount = float(input("Deposit amount: $"))
        if amount > 0:
            balance += amount
            transactions.append(f"Deposited ${amount:.2f}")
            print("Deposit successful.")
        else:
            print("Invalid amount.")

    elif choice == "3":
        amount = float(input("Withdraw amount: $"))
        if 0 < amount <= balance:
            balance -= amount
            transactions.append(f"Withdrew ${amount:.2f}")
            print("Withdrawal successful.")
        else:
            print("Invalid or insufficient funds.")

    elif choice == "4":
        if has_savings:
            print("Savings account already exists.")
        else:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            if age >= 18:
                has_savings = True
                savings_balance = 0.0
                print(f"Savings account created for {name}.")
            else:
                print("Must be 18+ to open a savings account.")

    elif choice == "5":
        if not has_savings:
            print("No savings account found.")
            continue

        while True:
            print("\n--- Savings Menu ---")
            print("1. Deposit to savings")
            print("2. Withdraw from savings")
            print("3. Check savings balance")
            print("4. Back to main menu")

            s_choice = input("Choose (1-4): ")

            if s_choice == "1":
                amount = float(input("Amount: $"))
                if 0 < amount <= balance:
                    balance -= amount
                    savings_balance += amount
                    transactions.append(f"Moved ${amount:.2f} to savings")
                    print("Deposited to savings.")
                else:
                    print("Invalid amount.")

            elif s_choice == "2":
                amount = float(input("Amount: $"))
                if 0 < amount <= savings_balance:
                    savings_balance -= amount
                    balance += amount
                    transactions.append(
                        f"Moved ${amount:.2f} from savings to main balance")
                    print("Withdrawn from savings.")
                else:
                    print("Insufficient savings.")

            elif s_choice == "3":
                print(f"Savings balance: ${savings_balance:.2f}")

            elif s_choice == "4":
                break

            else:
                print("Invalid choice.")

    elif choice == "6":
        if not transactions:
            print("No transactions yet.")
        else:
            print("\n--- Transaction History ---")
            for i, t in enumerate(transactions, start=1):
                print(f"{i}. {t}")

    elif choice == "7":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid option.")
